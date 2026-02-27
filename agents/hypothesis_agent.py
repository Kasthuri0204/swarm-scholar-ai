import os


from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def hypothesis_agent(topic, field_data, summary, critique, debate):
    field = field_data["field"]

    print("\n" + "=" * 60)
    print("AGENT 4 - Hypothesis Agent ACTIVATED")
    print(f"Field: {field}")
    print("=" * 60)

    prompt = f"""You are a Research Hypothesis Agent specializing in {field}.

Your job is to propose novel, evidence-grounded research directions and hypotheses
based on the gaps and contradictions found by previous agents.

TOPIC: {topic}

LITERATURE SUMMARY:
{summary}

IDENTIFIED GAPS AND WEAKNESSES:
{critique}

DEBATE RESOLUTIONS:
{debate}

Based on all of the above, generate novel research hypotheses in this exact format:

NOVEL HYPOTHESIS 1:
- Statement: (clear, testable hypothesis statement)
- Grounded In: (which gap or contradiction this addresses)
- Theoretical Basis: (why this is theoretically sound)
- Suggested Method: (how this could be tested)

NOVEL HYPOTHESIS 2:
- Statement:
- Grounded In:
- Theoretical Basis:
- Suggested Method:

NOVEL HYPOTHESIS 3:
- Statement:
- Grounded In:
- Theoretical Basis:
- Suggested Method:

INNOVATION OPPORTUNITIES:
- Opportunity 1 for a breakthrough in this field
- Opportunity 2 that combines this with another domain

RECOMMENDED NEXT STEPS:
- Step 1 for a researcher wanting to pursue this
- Step 2 to validate the hypotheses above

Rules:
- Hypotheses must be grounded in the evidence — not random ideas
- Each hypothesis must be specific and testable
- Total response under 400 words"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    hypotheses = response.choices[0].message.content
    print("Hypotheses Generated.")
    return hypotheses