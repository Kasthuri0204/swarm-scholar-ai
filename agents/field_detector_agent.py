import os
import time
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SUPPORTED_FIELDS = [
    "Medical & Healthcare",
    "Internet of Things & Smart Technology",
    "Artificial Intelligence & Machine Learning",
    "Environmental & Climate Science",
    "Social Science & Humanities",
    "Business & Economics",
    "Cybersecurity",
    "Robotics & Automation",
    "Education & E-Learning",
    "General Engineering"
]

def generate_custom_prompt(topic, field, prompt_type):
    """
    Dynamically generates a custom prompt template
    for unknown research fields using AI!
    """
    print(f"\n🧠 Auto-generating custom {prompt_type} prompt for: {field}...")

    if prompt_type == "literature":
        instruction = f"""You are a prompt engineering expert.

Create a structured literature review prompt template for the research field: '{field}'
Related to topic: '{topic}'

Generate a prompt template with 7 relevant sections using this exact format:
- Each section must start with a relevant emoji
- Each section must have a clear title in CAPS
- Each section must have a description in [square brackets]

Example format:
📌 OVERVIEW
[Brief introduction]

🔬 KEY FINDINGS
[5 important findings]

Make the sections highly specific and relevant to the '{field}' field.
Return ONLY the template sections. No extra explanation."""

    else:  # critic
        instruction = f"""You are a prompt engineering expert.

Create a structured critical analysis prompt template for the research field: '{field}'
Related to topic: '{topic}'

Generate a prompt template with 7 relevant sections using this exact format:
- Each section must start with a relevant emoji
- Each section must have a clear title in CAPS
- Each section must have a description in [square brackets]

Example format:
⚠️ RESEARCH GAPS
[4 specific gaps]

❌ LIMITATIONS
[4 weaknesses]

Make the sections highly specific and relevant to critically analyzing '{field}' research.
Return ONLY the template sections. No extra explanation."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": instruction}]
    )

    custom_template = response.choices[0].message.content
    print(f"✅ Custom prompt generated for {field}!")
    return custom_template


def detect_field(topic):
    print("\n" + "=" * 60)
    print("🤖 AGENT 0 - Field Detector Agent ACTIVATED")
    print("=" * 60)
    print("🔍 Analyzing research topic...")
    print("🧠 Identifying research domain...")
    time.sleep(1)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{
            "role": "user",
            "content": f"""You are a Research Field Classification Agent.

Analyze this research topic: '{topic}'

First try to match with one of these known fields:
{chr(10).join(f"- {field}" for field in SUPPORTED_FIELDS)}

If it matches one of the above, reply with EXACTLY that field name.
If it does NOT match any field, reply with:
UNKNOWN: [most appropriate field name for this topic]

Reply with ONLY the field name or UNKNOWN: field. Nothing else."""
        }]
    )

    detected = response.choices[0].message.content.strip()

    # Check if it's an unknown field
    if detected.upper().startswith("UNKNOWN:"):
        unknown_field = detected.split(":", 1)[1].strip()
        print(f"⚠️  Unknown field detected: {unknown_field}")
        print("🤖 Activating Auto Prompt Generator...")
        time.sleep(1)

        # Auto generate custom prompts for this unknown field
        custom_lit_prompt = generate_custom_prompt(
            topic, unknown_field, "literature")
        custom_critic_prompt = generate_custom_prompt(
            topic, unknown_field, "critic")

        return {
            "field": unknown_field,
            "is_custom": True,
            "literature_prompt": custom_lit_prompt,
            "critic_prompt": custom_critic_prompt
        }

    # Try to match known field
    matched_field = None
    for field in SUPPORTED_FIELDS:
        if field.lower() in detected.lower():
            matched_field = field
            break

    if matched_field:
        print(f"✅ Research Field Detected: {matched_field}")
        return {
            "field": matched_field,
            "is_custom": False,
            "literature_prompt": None,
            "critic_prompt": None
        }

    # Safe fallback
    print(f"✅ Research Field: General Engineering (fallback)")
    return {
        "field": "General Engineering",
        "is_custom": False,
        "literature_prompt": None,
        "critic_prompt": None
    }