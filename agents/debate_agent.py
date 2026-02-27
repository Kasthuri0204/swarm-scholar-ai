import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def debate_agent(topic, field_data, papers, summary, critique):
    field = field_data["field"]

    print("\n" + "=" * 60)
    print("AGENT 3 - Debate Agent ACTIVATED")
    print(f"Field: {field}")
    print("=" * 60)

    from rag.paper_fetcher import format_papers_for_prompt
    papers_text = format_papers_for_prompt(papers)

    prompt = f"""You are a Research Debate Agent specializing in {field}.

Your job is to identify contradictions between papers, debate both sides, and resolve them.

TOPIC: {topic}

PAPERS:
{papers_text}

CRITIC'S IDENTIFIED CONTRADICTIONS:
{critique}

For each contradiction found, provide a structured debate in this format:

CONTRADICTION 1:
- Claim A: (what one paper/group claims)
- Claim B: (what another paper/group claims)
- Evidence for A: (specific evidence)
- Evidence for B: (specific evidence)
- Resolution: (which is better supported and why, or if both are valid in different contexts)

CONTRADICTION 2 (if present):
- Claim A:
- Claim B:
- Evidence for A:
- Evidence for B:
- Resolution:

OVERALL CONSENSUS:
One paragraph summarizing what the research community broadly agrees on despite the contradictions.

REFINED UNDERSTANDING:
One sentence stating the most defensible position based on the evidence.

Rules:
- Be specific — reference actual papers
- Keep resolutions evidence-based, not opinion-based
- Total response under 350 words"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    debate = response.choices[0].message.content
    print("Debate Analysis Generated.")
    return debate