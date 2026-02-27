import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def report_agent(topic, field_data, papers, summary, critique, debate, hypotheses):
    field = field_data["field"]

    print("\n" + "=" * 60)
    print("AGENT 5 - Report Agent ACTIVATED")
    print(f"Field: {field}")
    print("=" * 60)

    from rag.paper_fetcher import format_citations
    citations = format_citations(papers)

    prompt = f"""You are a Research Report Agent specializing in {field}.

Your job is to compile all agent outputs into one final, polished research report.

TOPIC: {topic}
FIELD: {field}
PAPERS ANALYSED: {len(papers)}

LITERATURE SUMMARY:
{summary}

CRITICAL ANALYSIS:
{critique}

DEBATE RESOLUTIONS:
{debate}

NOVEL HYPOTHESES:
{hypotheses}

Write a final structured research report in this format:

EXECUTIVE SUMMARY:
2-3 sentences summarizing the entire research landscape and key takeaway.

KEY CONTRIBUTIONS OF THIS ANALYSIS:
- Contribution 1
- Contribution 2
- Contribution 3

MAIN FINDINGS:
- Finding 1
- Finding 2
- Finding 3

CRITICAL GAPS IDENTIFIED:
- Gap 1
- Gap 2

RESOLVED CONTRADICTIONS:
- Resolution 1
- Resolution 2

PROPOSED RESEARCH DIRECTIONS:
- Direction 1
- Direction 2
- Direction 3

SELF-CRITIQUE OF THIS ANALYSIS:
One honest paragraph about the limitations of this AI-generated analysis and what a human researcher should verify.

Rules:
- This is a SYNTHESIS — do not repeat everything word for word
- Be concise, professional, and academically rigorous
- Total response under 450 words"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    report = response.choices[0].message.content
    print("Final Report Generated.")
    return report, citations