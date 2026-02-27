import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def critic_agent(topic, field_data, papers, summary):
    field = field_data["field"]

    print("\n" + "=" * 60)
    print("AGENT 2 - Critic Agent ACTIVATED")
    print(f"Field: {field}")
    print("=" * 60)

    from rag.paper_fetcher import format_papers_for_prompt
    papers_text = format_papers_for_prompt(papers)

    prompt = f"""You are a Senior Research Critic specializing in {field}.

You have access to {len(papers)} research papers on '{topic}' and their literature summary.

PAPERS:
{papers_text}

LITERATURE SUMMARY:
{summary}

Provide a critical analysis in this exact format:

RESEARCH GAPS:
- Gap 1 not addressed in any of the papers
- Gap 2 missing from current research

WEAKNESSES:
- Weakness 1 observed across the papers
- Weakness 2 in the methodologies used

UNRESOLVED QUESTIONS:
- Question 1 left unanswered by these papers
- Question 2 that needs further investigation

CONTRADICTIONS FOUND:
- Contradiction between Paper X and Paper Y (be specific)
- Another conflicting finding if present

FUTURE RESEARCH DIRECTIONS:
- Direction 1 based on identified gaps
- Direction 2 that could advance the field

Rules:
- Be specific — reference actual paper titles or numbers
- Keep each point to one clear sentence
- Total response under 300 words"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    critique = response.choices[0].message.content
    print("Critical Analysis Generated.")
    return critique