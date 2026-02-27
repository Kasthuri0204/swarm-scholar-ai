# ═══════════════════════════════════════════════════════════
# components.py — SwarmScholar AI
# All HTML blocks, cards, layouts live here
# ═══════════════════════════════════════════════════════════

def get_styles():
    return """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');

:root {
    --navy:        #0D1B2A;
    --navy-mid:    #1B2E45;
    --navy-card:   #162032;
    --blue:        #1E6FFF;
    --blue-bright: #4D8EFF;
    --blue-glow:   rgba(30,111,255,0.18);
    --blue-pale:   #EBF2FF;
    --teal:        #0EA5E9;
    --bg:          #F4F7FC;
    --bg-white:    #FFFFFF;
    --border:      #DDE5F0;
    --text-h:      #0D1B2A;
    --text-body:   #2C3E55;
    --text-muted:  #607080;
    --text-faint:  #9AAABB;
    --green:       #10B981;
    --green-bg:    #ECFDF5;
    --orange:      #F59E0B;
    --orange-bg:   #FFFBEB;
    --purple:      #8B5CF6;
    --purple-bg:   #F5F3FF;
    --red:         #EF4444;
    --red-bg:      #FEF2F2;
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, .stApp {
    font-family: 'Poppins', sans-serif !important;
    background: var(--bg) !important;
    -webkit-font-smoothing: antialiased;
}

/* ── Kill all Streamlit chrome ── */
.stApp > header,
[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="collapsedControl"],
section[data-testid="stSidebar"],
footer { display: none !important; height: 0 !important; }

.block-container { padding: 0 !important; margin: 0 !important; max-width: 100% !important; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-thumb { background: #C8D5E8; border-radius: 10px; }

/* ── Base button ── */
div.stButton > button {
    font-family: 'Poppins', sans-serif !important;
    font-weight: 600 !important;
    border: none !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
    letter-spacing: 0.2px !important;
}
div.stButton > button:focus { outline: none !important; box-shadow: none !important; }

/* Primary blue */
.btn-primary div.stButton > button {
    background: var(--blue) !important;
    color: #fff !important;
    font-size: 15px !important;
    font-weight: 700 !important;
    padding: 15px 0 !important;
    border-radius: 12px !important;
    width: 100% !important;
    box-shadow: 0 4px 20px rgba(30,111,255,0.38) !important;
}
.btn-primary div.stButton > button:hover {
    background: #155FE8 !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 28px rgba(30,111,255,0.48) !important;
}

/* Dark */
.btn-dark div.stButton > button {
    background: var(--navy) !important;
    color: #fff !important;
    font-size: 15px !important;
    font-weight: 700 !important;
    padding: 15px 0 !important;
    border-radius: 12px !important;
    width: 100% !important;
    box-shadow: 0 4px 16px rgba(13,27,42,0.3) !important;
    margin-top: 8px !important;
}
.btn-dark div.stButton > button:hover {
    background: var(--navy-mid) !important;
    transform: translateY(-2px) !important;
}

/* Ghost */
.btn-ghost div.stButton > button {
    background: transparent !important;
    color: var(--text-muted) !important;
    border: 1.5px solid var(--border) !important;
    font-size: 13px !important;
    padding: 9px 20px !important;
    border-radius: 10px !important;
    font-weight: 500 !important;
}
.btn-ghost div.stButton > button:hover {
    border-color: var(--blue) !important;
    color: var(--blue) !important;
    background: var(--blue-pale) !important;
    transform: none !important;
    box-shadow: none !important;
}

/* ── Input ── */
.stTextInput > div > div > input {
    font-family: 'Poppins', sans-serif !important;
    font-size: 15px !important;
    border: 2px solid var(--border) !important;
    border-radius: 12px !important;
    padding: 15px 20px !important;
    background: #fff !important;
    color: var(--text-h) !important;
}
.stTextInput > div > div > input:focus {
    border-color: var(--blue) !important;
    box-shadow: 0 0 0 4px var(--blue-glow) !important;
}
.stTextInput > div > div > input::placeholder { color: var(--text-faint) !important; }
.stTextInput > label {
    font-family: 'Poppins', sans-serif !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    color: var(--text-body) !important;
}

/* ── Download ── */
.stDownloadButton > button {
    font-family: 'Poppins', sans-serif !important;
    background: var(--navy) !important;
    color: #fff !important;
    font-weight: 700 !important;
    font-size: 14px !important;
    border-radius: 10px !important;
    border: none !important;
    padding: 13px 32px !important;
    box-shadow: 0 4px 14px rgba(13,27,42,0.28) !important;
    transition: all 0.2s !important;
}
.stDownloadButton > button:hover {
    background: var(--navy-mid) !important;
    transform: translateY(-2px) !important;
}

/* ── Spinner ── */
.stSpinner > div { border-top-color: var(--blue) !important; border-width: 3px !important; }

/* ── Alerts ── */
.stSuccess > div, .stWarning > div, .stError > div {
    font-family: 'Poppins', sans-serif !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    border-radius: 10px !important;
}
</style>
"""


# ── HELPERS ────────────────────────────────────────────────
def S(px): return f'<div style="height:{px}px;"></div>'
def HR():  return '<div style="height:1px;background:#DDE5F0;margin:30px 0;"></div>'

def tag(label, color="#1E6FFF", bg="#EBF2FF"):
    return (
        f'<div style="display:inline-block;font-family:Poppins,sans-serif;'
        f'font-size:10px;font-weight:700;letter-spacing:2.5px;'
        f'text-transform:uppercase;color:{color};background:{bg};'
        f'padding:5px 14px;border-radius:20px;margin-bottom:14px;">{label}</div>'
    )

def pill(label, color="#1E6FFF", bg="#EBF2FF"):
    return (
        f'<span style="display:inline-block;background:{bg};color:{color};'
        f'font-family:Poppins,sans-serif;font-size:11px;font-weight:700;'
        f'padding:4px 14px;border-radius:20px;letter-spacing:0.5px;">{label}</span>'
    )


# ── LOGO HELPER ────────────────────────────────────────────
def _logo_html(logo_b64, size=34, radius=9):
    """Returns <img> tag if logo_b64 provided, otherwise falls back to SVG swarm icon."""
    if logo_b64:
        return (
            f'<img src="data:image/png;base64,{logo_b64}" '
            f'style="width:{size}px;height:{size}px;border-radius:{radius}px;'
            f'object-fit:cover;display:block;" />'
        )
    # Fallback SVG icon
    icon_size = int(size * 0.53)
    return (
        f'<div style="width:{size}px;height:{size}px;'
        f'background:linear-gradient(135deg,#1E6FFF,#0EA5E9);'
        f'border-radius:{radius}px;display:flex;align-items:center;justify-content:center;">'
        f'<svg width="{icon_size}" height="{icon_size}" viewBox="0 0 24 24" fill="none">'
        f'<circle cx="12" cy="12" r="3" fill="white"/>'
        f'<circle cx="4" cy="6" r="2" fill="white" opacity="0.7"/>'
        f'<circle cx="20" cy="6" r="2" fill="white" opacity="0.7"/>'
        f'<circle cx="4" cy="18" r="2" fill="white" opacity="0.7"/>'
        f'<circle cx="20" cy="18" r="2" fill="white" opacity="0.7"/>'
        f'<line x1="12" y1="12" x2="4" y2="6" stroke="white" stroke-width="1" opacity="0.5"/>'
        f'<line x1="12" y1="12" x2="20" y2="6" stroke="white" stroke-width="1" opacity="0.5"/>'
        f'<line x1="12" y1="12" x2="4" y2="18" stroke="white" stroke-width="1" opacity="0.5"/>'
        f'<line x1="12" y1="12" x2="20" y2="18" stroke="white" stroke-width="1" opacity="0.5"/>'
        f'</svg></div>'
    )


# ── NAVBAR ─────────────────────────────────────────────────
def navbar(logo_b64=""):
    return (
        '<div style="background:#0D1B2A;padding:16px 64px;'
        'display:flex;justify-content:space-between;align-items:center;">'

        # Logo area
        '<div style="display:flex;align-items:center;gap:12px;">'
        + _logo_html(logo_b64, size=34, radius=9) +
        '<span style="font-family:Poppins,sans-serif;font-size:19px;font-weight:800;'
        'color:#FFFFFF;letter-spacing:-0.5px;">'
        'Swarm<span style="color:#4D8EFF;">Scholar</span></span>'
        '</div>'

        # Status badge
        '<div style="display:flex;align-items:center;gap:8px;">'
        '<div style="width:7px;height:7px;background:#10B981;border-radius:50%;'
        'box-shadow:0 0 8px rgba(16,185,129,0.7);"></div>'
        '<span style="font-family:Poppins,sans-serif;font-size:11px;font-weight:500;'
        'color:#4D6882;letter-spacing:1.8px;">AI RESEARCH COPILOT</span>'
        '</div>'
        '</div>'
    )


def research_navbar(logo_b64=""):
    return (
        '<div style="background:#0D1B2A;padding:16px 64px;'
        'display:flex;justify-content:space-between;align-items:center;">'

        '<div style="display:flex;align-items:center;gap:12px;">'
        + _logo_html(logo_b64, size=30, radius=8) +
        '<span style="font-family:Poppins,sans-serif;font-size:17px;font-weight:800;'
        'color:#FFFFFF;">Swarm<span style="color:#4D8EFF;">Scholar</span></span>'
        '</div>'

        '<span style="font-family:Poppins,sans-serif;font-size:10px;font-weight:600;'
        'color:#3D566E;letter-spacing:2.5px;">RESEARCH CONSOLE</span>'
        '</div>'
    )


# ── HERO ───────────────────────────────────────────────────
def hero(logo_b64=""):
    # Show large centered logo in hero only when a custom logo is provided
    logo_center = ""
    if logo_b64:
        logo_center = (
            '<div style="position:relative;margin-bottom:28px;">'
            f'<img src="data:image/png;base64,{logo_b64}" '
            'style="width:80px;height:80px;border-radius:20px;'
            'object-fit:cover;box-shadow:0 8px 32px rgba(30,111,255,0.35);" />'
            '</div>'
        )

    return (
        '<div style="background:linear-gradient(165deg,#07111E 0%,#0D1B2A 45%,#0F2744 100%);'
        'padding:108px 64px 72px;text-align:center;position:relative;overflow:hidden;">'

        # Radial glow
        '<div style="position:absolute;top:-100px;left:50%;transform:translateX(-50%);'
        'width:800px;height:500px;'
        'background:radial-gradient(ellipse,rgba(30,111,255,0.16) 0%,transparent 65%);'
        'pointer-events:none;"></div>'

        # Grid dots
        '<div style="position:absolute;inset:0;'
        'background-image:radial-gradient(rgba(255,255,255,0.03) 1px,transparent 1px);'
        'background-size:30px 30px;pointer-events:none;"></div>'

        + logo_center +

        # Badge
        '<div style="position:relative;display:inline-flex;align-items:center;gap:9px;'
        'background:rgba(30,111,255,0.10);border:1px solid rgba(77,142,255,0.22);'
        'padding:7px 20px;border-radius:30px;margin-bottom:30px;">'
        '<div style="width:6px;height:6px;background:#4D8EFF;border-radius:50%;'
        'box-shadow:0 0 10px rgba(77,142,255,0.9);"></div>'
        '<span style="font-family:Poppins,sans-serif;font-size:11px;font-weight:600;'
        'color:#93BBFF;letter-spacing:1.8px;">LLaMA 3.3 · 70B · Groq API · Semantic Scholar</span>'
        '</div>'

        # H1
        '<div style="position:relative;font-family:Poppins,sans-serif;font-size:56px;'
        'font-weight:800;color:#F1F7FF;line-height:1.1;letter-spacing:-1.8px;margin-bottom:22px;">'
        'AI Research Swarm<br>'
        '<span style="color:#4D8EFF;">Copilot</span>'
        '</div>'

        # Sub
        '<div style="position:relative;font-family:Poppins,sans-serif;font-size:17px;'
        'color:#7FA3C8;max-width:560px;margin:0 auto;line-height:1.8;font-weight:300;">'
        'Five AI agents autonomously fetch real research papers, analyze literature, '
        'debate contradictions, generate hypotheses, and deliver a complete report — instantly.'
        '</div>'
        '</div>'

        # CTA strip
        '<div style="background:linear-gradient(165deg,#0F2744 0%,#0D1B2A 100%);'
        'padding:0 0 60px;"></div>'
    )


# ── STATS BAR ──────────────────────────────────────────────
def stats_bar():
    def s(v, l):
        return (
            f'<div style="text-align:center;padding:0 10px;">'
            f'<div style="font-family:Poppins,sans-serif;font-size:36px;'
            f'font-weight:800;color:#0D1B2A;line-height:1;">{v}</div>'
            f'<div style="font-family:Poppins,sans-serif;font-size:10px;font-weight:600;'
            f'color:#607080;letter-spacing:1.8px;text-transform:uppercase;margin-top:7px;">'
            f'{l}</div></div>'
        )
    d = '<div style="width:1px;height:50px;background:#DDE5F0;"></div>'
    return (
        '<div style="background:#FFFFFF;border-top:1px solid #DDE5F0;'
        'border-bottom:1px solid #DDE5F0;padding:46px 64px;'
        'display:flex;justify-content:center;align-items:center;gap:60px;">'
        + s("5","AI Agents") + d
        + s("10+","Research Fields") + d
        + s("&#8734;","Topics") + d
        + s("70B","Parameters") + d
        + s("RAG","Real Papers")
        + '</div>'
    )


# ── ABOUT SECTION ──────────────────────────────────────────
def about_section():
    return (
        '<div style="background:#F4F7FC;padding:80px 64px 60px;">'

        '<div style="text-align:center;margin-bottom:52px;">'
        + tag("What is SwarmScholar?") +
        '<div style="font-family:Poppins,sans-serif;font-size:32px;font-weight:800;'
        'color:#0D1B2A;letter-spacing:-0.5px;margin-bottom:12px;">'
        'A Swarm of AI Agents That Think Like Researchers</div>'
        '<div style="font-family:Poppins,sans-serif;font-size:15px;color:#607080;'
        'max-width:580px;margin:0 auto;line-height:1.75;font-weight:400;">'
        'Built for DevHack 2026 Problem Statement AIPS06 — AI Research Copilot Swarm.'
        ' SwarmScholar simulates how a real research team collaborates.</div>'
        '</div>'

        '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px;">'

        '<div style="background:#FFFFFF;border-radius:16px;padding:32px 28px;'
        'border:1px solid #DDE5F0;border-top:4px solid #1E6FFF;">'
        '<div style="font-size:28px;margin-bottom:14px;">🔍</div>'
        '<div style="font-family:Poppins,sans-serif;font-size:16px;font-weight:700;'
        'color:#0D1B2A;margin-bottom:8px;">Real Paper Analysis</div>'
        '<div style="font-family:Poppins,sans-serif;font-size:13px;color:#607080;'
        'line-height:1.7;">Fetches real academic papers from Semantic Scholar API. '
        'Every insight is grounded in actual research, not assumptions.</div>'
        '</div>'

        '<div style="background:#FFFFFF;border-radius:16px;padding:32px 28px;'
        'border:1px solid #DDE5F0;border-top:4px solid #10B981;">'
        '<div style="font-size:28px;margin-bottom:14px;">🤝</div>'
        '<div style="font-family:Poppins,sans-serif;font-size:16px;font-weight:700;'
        'color:#0D1B2A;margin-bottom:8px;">Multi-Agent Debate</div>'
        '<div style="font-family:Poppins,sans-serif;font-size:13px;color:#607080;'
        'line-height:1.7;">Agents critique each other\'s outputs, debate contradictions, '
        'and refine understanding — just like a real research team.</div>'
        '</div>'

        '<div style="background:#FFFFFF;border-radius:16px;padding:32px 28px;'
        'border:1px solid #DDE5F0;border-top:4px solid #8B5CF6;">'
        '<div style="font-size:28px;margin-bottom:14px;">💡</div>'
        '<div style="font-family:Poppins,sans-serif;font-size:16px;font-weight:700;'
        'color:#0D1B2A;margin-bottom:8px;">Novel Hypotheses</div>'
        '<div style="font-family:Poppins,sans-serif;font-size:13px;color:#607080;'
        'line-height:1.7;">Identifies gaps in current research and proposes testable '
        'hypotheses grounded in evidence and theoretical coherence.</div>'
        '</div>'

        '</div></div>'
    )


# ── PIPELINE SECTION ───────────────────────────────────────
def pipeline_section():
    agents = [
        ("#1E6FFF", "#EBF2FF", "Agent 00", "Field Detector",
         "Identifies the research domain and auto-generates field-specific prompt templates."),
        ("#0EA5E9", "#E0F7FF", "RAG Layer", "Paper Fetcher",
         "Queries Semantic Scholar API and retrieves real papers with abstracts and citations."),
        ("#10B981", "#ECFDF5", "Agent 01", "Literature Agent",
         "Reads all fetched papers and produces a structured, field-specific literature summary."),
        ("#F59E0B", "#FFFBEB", "Agent 02", "Critic Agent",
         "Identifies gaps, weaknesses, contradictions, and unresolved questions across papers."),
        ("#EF4444", "#FEF2F2", "Agent 03", "Debate Agent",
         "Debates contradictions between papers and resolves them with evidence-based reasoning."),
        ("#8B5CF6", "#F5F3FF", "Agent 04", "Hypothesis Agent",
         "Proposes novel, testable research hypotheses grounded in identified gaps."),
        ("#0D1B2A", "#E8EEF5", "Agent 05", "Report Agent",
         "Compiles all outputs into a final structured report with citations and self-critique."),
    ]

    cards_html = ""
    for color, bg, num, name, desc in agents:
        cards_html += (
            f'<div style="background:#FFFFFF;border-radius:14px;padding:22px 24px;'
            f'border:1px solid #DDE5F0;border-left:4px solid {color};'
            f'display:flex;align-items:flex-start;gap:16px;">'
            f'<div style="background:{bg};color:{color};font-family:Poppins,sans-serif;'
            f'font-size:10px;font-weight:700;padding:5px 12px;border-radius:20px;'
            f'white-space:nowrap;letter-spacing:1px;margin-top:2px;">{num}</div>'
            f'<div>'
            f'<div style="font-family:Poppins,sans-serif;font-size:15px;font-weight:700;'
            f'color:#0D1B2A;margin-bottom:4px;">{name}</div>'
            f'<div style="font-family:Poppins,sans-serif;font-size:13px;color:#607080;'
            f'line-height:1.65;font-weight:400;">{desc}</div>'
            f'</div></div>'
        )

    return (
        '<div style="background:#FFFFFF;padding:80px 64px;'
        'border-top:1px solid #DDE5F0;border-bottom:1px solid #DDE5F0;">'
        '<div style="text-align:center;margin-bottom:52px;">'
        + tag("The Pipeline", "#10B981", "#ECFDF5") +
        '<div style="font-family:Poppins,sans-serif;font-size:32px;font-weight:800;'
        'color:#0D1B2A;letter-spacing:-0.5px;">'
        'How the Swarm Works</div>'
        '</div>'
        '<div style="max-width:760px;margin:0 auto;'
        'display:flex;flex-direction:column;gap:14px;">'
        + cards_html +
        '</div></div>'
    )


# ── BOTTOM CTA ─────────────────────────────────────────────
def bottom_cta():
    return (
        '<div style="background:linear-gradient(165deg,#07111E 0%,#0D1B2A 60%,#0F2744 100%);'
        'padding:90px 64px 48px;text-align:center;position:relative;overflow:hidden;">'
        '<div style="position:absolute;bottom:-80px;right:-60px;width:360px;height:360px;'
        'background:radial-gradient(circle,rgba(30,111,255,0.12) 0%,transparent 65%);'
        'pointer-events:none;"></div>'
        '<div style="position:relative;font-family:Poppins,sans-serif;font-size:38px;'
        'font-weight:800;color:#F1F7FF;letter-spacing:-0.8px;margin-bottom:14px;">'
        'Ready to Explore Research?</div>'
        '<div style="position:relative;font-family:Poppins,sans-serif;font-size:15px;'
        'color:#4D6882;font-weight:300;margin-bottom:0;">'
        'Real papers. 5 AI agents. Complete analysis. Instant report.'
        '</div></div>'
    )


# ── FOOTER ─────────────────────────────────────────────────
def footer():
    return (
        '<div style="background:#050E18;padding:28px 64px;'
        'display:flex;justify-content:space-between;align-items:center;">'
        '<span style="font-family:Poppins,sans-serif;font-size:13px;'
        'font-weight:700;color:#FFFFFF;">'
        'Swarm<span style="color:#4D8EFF;">Scholar</span> AI</span>'
        '<span style="font-family:Poppins,sans-serif;font-size:11px;color:#2C4057;">'
        'Multi-Agent Research Copilot &nbsp;&middot;&nbsp; LLaMA 3.3 70B &nbsp;&middot;&nbsp; Groq &nbsp;&middot;&nbsp; Semantic Scholar'
        '</span>'
        '<span style="font-family:Poppins,sans-serif;font-size:11px;color:#2C4057;">'
        'DevHack 2026 &nbsp;&middot;&nbsp; AIPS06'
        '</span>'
        '</div>'
    )


# ── RESEARCH PAGE COMPONENTS ───────────────────────────────

def page_title_block():
    return (
        '<div style="margin-bottom:30px;">'
        + tag("Research Console") +
        '<div style="font-family:Poppins,sans-serif;font-size:28px;font-weight:800;'
        'color:#0D1B2A;letter-spacing:-0.5px;margin-bottom:8px;">'
        'What do you want to explore?</div>'
        '<div style="font-family:Poppins,sans-serif;font-size:14px;'
        'color:#607080;font-weight:400;line-height:1.6;">'
        'Enter any topic — real papers are fetched and 5 agents analyse them for you.'
        '</div></div>'
    )


def results_wrapper_open():
    return (
        '<div style="background:#EEF3FB;border:1.5px solid #C8D8F0;'
        'border-radius:20px;padding:30px;">'
        '<div style="font-family:Poppins,sans-serif;font-size:10px;font-weight:700;'
        'letter-spacing:2.5px;text-transform:uppercase;color:#607080;'
        'margin-bottom:24px;">Analysis Results</div>'
    )


def results_wrapper_close():
    return '</div>'


def info_strip(label, content_html, accent="#1E6FFF"):
    return (
        f'<div style="background:#FFFFFF;border:1px solid #DDE5F0;'
        f'border-left:4px solid {accent};border-radius:12px;'
        f'padding:14px 20px;margin-bottom:12px;'
        f'display:flex;align-items:center;gap:16px;">'
        f'<div style="font-family:Poppins,sans-serif;font-size:10px;font-weight:700;'
        f'color:#9AAABB;letter-spacing:1.5px;text-transform:uppercase;white-space:nowrap;">'
        f'{label}</div>'
        f'<div style="width:1px;height:20px;background:#DDE5F0;flex-shrink:0;"></div>'
        f'{content_html}'
        f'</div>'
    )


def agent_result_card(num_label, title, badge, badge_bg, badge_color, top_color, body_html):
    return (
        f'<div style="background:#FFFFFF;border:1px solid #DDE5F0;'
        f'border-top:4px solid {top_color};border-radius:16px;'
        f'padding:26px 28px;margin-bottom:12px;'
        f'box-shadow:0 2px 10px rgba(0,0,0,0.04);">'

        f'<div style="display:flex;justify-content:space-between;align-items:flex-start;'
        f'margin-bottom:18px;padding-bottom:14px;border-bottom:1px solid #F0F4FA;">'
        f'<div>'
        f'<div style="font-family:Poppins,sans-serif;font-size:10px;font-weight:600;'
        f'color:#9AAABB;letter-spacing:2px;text-transform:uppercase;margin-bottom:4px;">'
        f'{num_label}</div>'
        f'<div style="font-family:Poppins,sans-serif;font-size:16px;font-weight:700;'
        f'color:#0D1B2A;">{title}</div>'
        f'</div>'
        f'<div style="background:{badge_bg};color:{badge_color};'
        f'font-family:Poppins,sans-serif;font-size:10px;font-weight:700;'
        f'padding:5px 13px;border-radius:20px;letter-spacing:0.8px;'
        f'white-space:nowrap;">{badge}</div>'
        f'</div>'

        + body_html +
        f'</div>'
    )


def download_card(short_topic, paper_count):
    return (
        '<div style="background:linear-gradient(135deg,#0D1B2A,#1B2E45);'
        'border-radius:16px;padding:26px 28px;margin-bottom:12px;'
        'display:flex;justify-content:space-between;align-items:center;">'
        '<div>'
        '<div style="font-family:Poppins,sans-serif;font-size:16px;font-weight:700;'
        'color:#F1F7FF;margin-bottom:6px;">Full Research Report Ready</div>'
        '<div style="font-family:Poppins,sans-serif;font-size:12px;color:#4D8EFF;'
        'margin-bottom:4px;">5 Agents &nbsp;·&nbsp; ' + str(paper_count) + ' Real Papers &nbsp;·&nbsp; Citations Included</div>'
        '<div style="font-family:Poppins,sans-serif;font-size:12px;color:#607080;">'
        'Topic: <span style="color:#93BBFF;">' + short_topic + '</span></div>'
        '</div>'
        '<div style="background:#10B981;color:#FFFFFF;font-family:Poppins,sans-serif;'
        'font-size:10px;font-weight:700;padding:6px 16px;border-radius:20px;'
        'letter-spacing:1px;">&#10003; COMPLETE</div>'
        '</div>'
    )


def citations_block(citations_text):
    return (
        '<div style="background:#F4F7FC;border:1px solid #DDE5F0;'
        'border-radius:12px;padding:20px 24px;margin-top:16px;">'
        '<div style="font-family:Poppins,sans-serif;font-size:10px;font-weight:700;'
        'letter-spacing:2px;text-transform:uppercase;color:#1E6FFF;margin-bottom:12px;">'
        'References</div>'
        '<pre style="font-family:Poppins,sans-serif;font-size:12px;'
        'color:#2C3E55;line-height:2;white-space:pre-wrap;margin:0;">'
        + citations_text +
        '</pre></div>'
    )