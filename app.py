import streamlit as st
import os
import base64

# ── UI Modules ──
import components
from components import (
    navbar, research_navbar, hero, stats_bar,
    about_section, pipeline_section,
    bottom_cta, footer,
    page_title_block, results_wrapper_open, results_wrapper_close,
    info_strip, agent_result_card, download_card, citations_block,
    S, HR
)

# ── Agents ──
from agents.field_detector_agent import detect_field
from agents.literature_agent import literature_agent
from agents.critic_agent import critic_agent
from agents.debate_agent import debate_agent
from agents.hypothesis_agent import hypothesis_agent
from agents.report_agent import report_agent

# ── RAG + Utils ──
from rag.paper_fetcher import fetch_papers, format_citations
from utils.file_saver import save_output


# ════════════════════════════════════════════════════════
# LOAD LOGO — reads logo.png from project root
# ════════════════════════════════════════════════════════
def get_logo_b64():
    try:
        with open("logo.png", "rb") as f:
            return base64.b64encode(f.read()).decode()
    except FileNotFoundError:
        return ""   # fallback: shows SVG icon if logo.png not found


# ════════════════════════════════════════════════════════
# CONFIG
# ════════════════════════════════════════════════════════
st.set_page_config(
    page_title="SwarmScholar AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "page" not in st.session_state:
    st.session_state.page = "landing"

# Load logo once at startup
LOGO = get_logo_b64()

st.markdown(components.get_styles(), unsafe_allow_html=True)


# ════════════════════════════════════════════════════════
# FORMAT AGENT OUTPUT → Clean HTML bullets
# ════════════════════════════════════════════════════════
def fmt(raw):
    lines = raw.strip().split('\n')
    html = ""
    current_sec = [None]
    current_items = []

    def flush():
        if not current_sec[0]:
            return ""
        rows = "".join(
            '<div style="display:flex;gap:11px;align-items:flex-start;margin-bottom:10px;">'
            '<div style="width:7px;height:7px;min-width:7px;background:#1E6FFF;'
            'border-radius:50%;margin-top:7px;flex-shrink:0;"></div>'
            '<div style="font-family:Poppins,sans-serif;font-size:14px;'
            'color:#2C3E55;line-height:1.7;font-weight:400;">' + i + '</div>'
            '</div>'
            for i in current_items if i.strip()
        )
        out = (
            '<div style="margin-bottom:22px;">'
            '<div style="font-family:Poppins,sans-serif;font-size:10px;font-weight:700;'
            'letter-spacing:2px;text-transform:uppercase;color:#1E6FFF;'
            'margin-bottom:10px;padding-bottom:7px;border-bottom:2px solid #EBF2FF;">'
            + current_sec[0] + '</div>' + rows + '</div>'
        )
        current_sec[0] = None
        current_items.clear()
        return out

    for raw_line in lines:
        line = raw_line.strip()
        if not line:
            continue
        cleaned = line.rstrip(':').strip('*').strip('#').strip()
        is_h = False
        if line.endswith(':') and len(line) < 70 and not line.startswith('-'):
            is_h = True
        elif line.isupper() and 3 < len(line) < 70:
            is_h = True
        elif line.startswith('**') and line.endswith('**') and len(line) < 70:
            is_h = True
        elif line.startswith('###') or line.startswith('##'):
            is_h = True
            cleaned = line.lstrip('#').strip().rstrip(':')
        elif len(line) > 2 and line[0].isdigit() and line[1] in '.):' and line[2:].strip().isupper():
            is_h = True
            cleaned = line[2:].strip().rstrip(':')
        if is_h:
            html += flush()
            current_sec[0] = cleaned
            current_items.clear()
        elif line.startswith(('- ', '• ', '* ')):
            current_items.append(line.lstrip('-•* ').strip())
        elif len(line) > 2 and line[0].isdigit() and line[1] in '.):':
            current_items.append(line[2:].strip())
        else:
            if current_sec[0] is not None:
                current_items.append(line)
            else:
                html += (
                    '<div style="font-family:Poppins,sans-serif;font-size:14px;'
                    'color:#2C3E55;line-height:1.75;margin-bottom:10px;">'
                    + line + '</div>'
                )
    html += flush()
    return html


# ════════════════════════════════════════════════════════
# LANDING PAGE
# ════════════════════════════════════════════════════════
def landing_page():

    # Navbar — pass logo base64
    st.markdown(navbar(LOGO), unsafe_allow_html=True)

    # Hero — pass logo base64 for centered display
    st.markdown(hero(LOGO), unsafe_allow_html=True)

    # Hero CTA button
    _, c, _ = st.columns([4, 1, 4])
    with c:
        st.markdown('<div class="btn-primary">', unsafe_allow_html=True)
        if st.button("Start Researching →", use_container_width=True, key="cta_hero"):
            st.session_state.page = "research"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(stats_bar(),        unsafe_allow_html=True)
    st.markdown(about_section(),    unsafe_allow_html=True)
    st.markdown(pipeline_section(), unsafe_allow_html=True)
    st.markdown(bottom_cta(),       unsafe_allow_html=True)

    # Bottom CTA button
    _, b, _ = st.columns([4, 1, 4])
    with b:
        st.markdown('<div class="btn-primary">', unsafe_allow_html=True)
        if st.button("Get Started →", use_container_width=True, key="cta_bottom"):
            st.session_state.page = "research"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(S(48),    unsafe_allow_html=True)
    st.markdown(footer(), unsafe_allow_html=True)


# ════════════════════════════════════════════════════════
# RESEARCH PAGE
# ════════════════════════════════════════════════════════
def research_page():

    # Navbar — pass logo base64
    st.markdown(research_navbar(LOGO), unsafe_allow_html=True)

    _, center, _ = st.columns([1, 2.6, 1])

    with center:
        st.markdown(S(36), unsafe_allow_html=True)

        # Back button
        st.markdown('<div class="btn-ghost">', unsafe_allow_html=True)
        if st.button("← Back to Home"):
            st.session_state.page = "landing"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown(S(26), unsafe_allow_html=True)
        st.markdown(page_title_block(), unsafe_allow_html=True)

        # Topic input
        topic = st.text_input(
            "Research Topic",
            placeholder="e.g. Machine Learning in Drug Discovery, IoT in Smart Cities..."
        )

        # Analyse button
        st.markdown('<div class="btn-dark">', unsafe_allow_html=True)
        run = st.button("Analyse Topic →", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown(HR(), unsafe_allow_html=True)

        # ── PIPELINE ──────────────────────────────────
        if run and topic.strip():

            st.markdown(results_wrapper_open(), unsafe_allow_html=True)

            # Agent 0 — Field Detection
            with st.spinner("Detecting research field..."):
                field_data = detect_field(topic)
            field     = field_data["field"]
            is_custom = field_data["is_custom"]

            field_pill = (
                f'<span style="background:{"#ECFDF5" if not is_custom else "#F5F3FF"};'
                f'color:{"#065F46" if not is_custom else "#5B21B6"};'
                f'font-family:Poppins,sans-serif;font-size:12px;font-weight:700;'
                f'padding:4px 14px;border-radius:20px;">'
                f'{"" if not is_custom else "Auto-Generated: "}{field}</span>'
                f'<span style="font-family:Poppins,sans-serif;font-size:12px;'
                f'color:#9AAABB;margin-left:10px;">'
                f'{"Domain identified." if not is_custom else "Custom prompts generated."}'
                f'</span>'
            )
            st.markdown(
                info_strip("Field", field_pill,
                           "#10B981" if not is_custom else "#8B5CF6"),
                unsafe_allow_html=True
            )

            # RAG — Fetch Papers
            with st.spinner("Fetching real research papers from Semantic Scholar..."):
                papers = fetch_papers(topic)

            if not papers:
                st.error("No papers found. Please try a more specific topic.")
                st.markdown(results_wrapper_close(), unsafe_allow_html=True)
                return

            papers_pill = (
                f'<span style="background:#EBF2FF;color:#1E4FAA;'
                f'font-family:Poppins,sans-serif;font-size:12px;font-weight:700;'
                f'padding:4px 14px;border-radius:20px;">{len(papers)} Papers Found</span>'
                f'<span style="font-family:Poppins,sans-serif;font-size:12px;'
                f'color:#9AAABB;margin-left:10px;">Fetched from Semantic Scholar</span>'
            )
            st.markdown(
                info_strip("Papers", papers_pill, "#1E6FFF"),
                unsafe_allow_html=True
            )

            # Agent 1 — Literature Review
            with st.spinner("Agent 01 — Reviewing literature from real papers..."):
                summary = literature_agent(topic, field_data, papers)
            st.markdown(
                agent_result_card(
                    "Agent 01", "Literature Review",
                    "LITERATURE", "#EBF2FF", "#1E4FAA",
                    "#1E6FFF", fmt(summary)
                ),
                unsafe_allow_html=True
            )

            # Agent 2 — Critical Analysis
            with st.spinner("Agent 02 — Running critical analysis..."):
                critique = critic_agent(topic, field_data, papers, summary)
            st.markdown(
                agent_result_card(
                    "Agent 02", "Critical Analysis",
                    "CRITIC", "#ECFDF5", "#065F46",
                    "#10B981", fmt(critique)
                ),
                unsafe_allow_html=True
            )

            # Agent 3 — Debate
            with st.spinner("Agent 03 — Debating contradictions across papers..."):
                debate = debate_agent(topic, field_data, papers, summary, critique)
            st.markdown(
                agent_result_card(
                    "Agent 03", "Debate & Contradiction Resolution",
                    "DEBATE", "#FFFBEB", "#92400E",
                    "#F59E0B", fmt(debate)
                ),
                unsafe_allow_html=True
            )

            # Agent 4 — Hypothesis
            with st.spinner("Agent 04 — Generating novel research hypotheses..."):
                hypotheses = hypothesis_agent(
                    topic, field_data, summary, critique, debate
                )
            st.markdown(
                agent_result_card(
                    "Agent 04", "Novel Hypotheses",
                    "HYPOTHESIS", "#F5F3FF", "#5B21B6",
                    "#8B5CF6", fmt(hypotheses)
                ),
                unsafe_allow_html=True
            )

            # Agent 5 — Final Report
            with st.spinner("Agent 05 — Compiling final research report..."):
                final_report, citations = report_agent(
                    topic, field_data, papers,
                    summary, critique, debate, hypotheses
                )
            st.markdown(
                agent_result_card(
                    "Agent 05", "Final Research Report",
                    "REPORT", "#F0F4FA", "#0D1B2A",
                    "#0D1B2A",
                    fmt(final_report) + citations_block(citations)
                ),
                unsafe_allow_html=True
            )

            # Save & Download
            filepath = save_output(
                topic, field,
                summary, critique, debate,
                hypotheses, final_report, citations
            )
            with open(filepath, 'r', encoding='utf-8') as f:
                report_content = f.read()

            short = topic[:48] + ('...' if len(topic) > 48 else '')
            st.markdown(download_card(short, len(papers)), unsafe_allow_html=True)
            st.markdown(S(12), unsafe_allow_html=True)
            st.download_button(
                label="⬇  Download Full Report",
                data=report_content,
                file_name=os.path.basename(filepath),
                mime="text/plain"
            )

            st.markdown(results_wrapper_close(), unsafe_allow_html=True)
            st.markdown(HR(), unsafe_allow_html=True)
            st.success("✅ All 5 agents completed. Full report is ready!")

        elif run and not topic.strip():
            st.warning("Please enter a research topic to continue.")

        st.markdown(S(60), unsafe_allow_html=True)

    st.markdown(footer(), unsafe_allow_html=True)


# ════════════════════════════════════════════════════════
# ROUTER
# ════════════════════════════════════════════════════════
if st.session_state.page == "landing":
    landing_page()
else:
    research_page()