import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def literature_agent(topic, field_data, papers):
    field = field_data["field"]

    print("\n" + "=" * 60)
    print("AGENT 1 - Literature Agent ACTIVATED")
    print(f"Field: {field} | Papers: {len(papers)}")
    print("=" * 60)

    from rag.paper_fetcher import format_papers_for_prompt
    papers_text = format_papers_for_prompt(papers)

    prompt = f"""You are an expert Academic Literature Research Agent specializing in {field}.

You have been given {len(papers)} real research papers on the topic: '{topic}'

{papers_text}

Based ONLY on these papers, provide a structured literature review in this exact format:

OVERVIEW:
One concise sentence introducing the research area based on the papers.

KEY FINDINGS:
- Finding 1 from the papers (cite which paper)
- Finding 2 from the papers (cite which paper)
- Finding 3 from the papers (cite which paper)

METHODOLOGIES USED:
- Method 1 identified across papers
- Method 2 identified across papers

CURRENT STATE OF RESEARCH:
One sentence on where this research stands based on these papers.

COMMON THEMES:
- Theme 1 appearing across multiple papers
- Theme 2 appearing across multiple papers

RESEARCH MATURITY:
One sentence on how mature/active this research field is based on citation counts and years.

Rules:
- Only reference information from the provided papers
- Keep each point to one clear sentence
- Total response under 350 words
- Be specific and cite paper numbers where relevant"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    summary = response.choices[0].message.content
    print("Literature Summary Generated.")
    return summary