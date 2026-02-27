import os
from datetime import datetime

def save_output(topic, field, summary, critique, debate, hypotheses, final_report, citations):
    os.makedirs("outputs", exist_ok=True)

    existing_files = sorted(
        [f for f in os.listdir("outputs") if f.endswith(".txt")],
        key=lambda x: os.path.getctime(os.path.join("outputs", x))
    )
    while len(existing_files) >= 2:
        os.remove(os.path.join("outputs", existing_files[0]))
        existing_files.pop(0)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_topic = topic[:20].replace(' ', '_')
    filename = f"outputs/SwarmScholar_{safe_topic}_{timestamp}.txt"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write("=" * 70 + "\n")
        f.write("   SwarmScholar AI — Multi-Agent Research Copilot\n")
        f.write("=" * 70 + "\n\n")
        f.write(f"Generated : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Topic     : {topic}\n")
        f.write(f"Field     : {field}\n\n")

        f.write("=" * 70 + "\n")
        f.write("AGENT 1 — LITERATURE REVIEW\n")
        f.write("=" * 70 + "\n\n")
        f.write(summary + "\n\n")

        f.write("=" * 70 + "\n")
        f.write("AGENT 2 — CRITICAL ANALYSIS\n")
        f.write("=" * 70 + "\n\n")
        f.write(critique + "\n\n")

        f.write("=" * 70 + "\n")
        f.write("AGENT 3 — DEBATE & CONTRADICTION RESOLUTION\n")
        f.write("=" * 70 + "\n\n")
        f.write(debate + "\n\n")

        f.write("=" * 70 + "\n")
        f.write("AGENT 4 — NOVEL HYPOTHESES\n")
        f.write("=" * 70 + "\n\n")
        f.write(hypotheses + "\n\n")

        f.write("=" * 70 + "\n")
        f.write("AGENT 5 — FINAL RESEARCH REPORT\n")
        f.write("=" * 70 + "\n\n")
        f.write(final_report + "\n\n")

        f.write("=" * 70 + "\n")
        f.write("REFERENCES\n")
        f.write("=" * 70 + "\n\n")
        f.write(citations + "\n")

    print(f"Report saved: {filename}")
    return filename