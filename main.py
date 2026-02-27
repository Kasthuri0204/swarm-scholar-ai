from agents.field_detector_agent import detect_field
from agents.literature_agent import literature_agent
from agents.critic_agent import critic_agent
from agents.debate_agent import debate_agent
from agents.hypothesis_agent import hypothesis_agent
from agents.report_agent import report_agent
from rag.paper_fetcher import fetch_papers
from utils.file_saver import save_output

def main():
    print("=" * 60)
    print("   SwarmScholar AI - Multi-Agent Research Copilot")
    print("=" * 60)

    topic = input("\nEnter your research topic: ")

    # Agent 0 — Field Detection
    field_data = detect_field(topic)

    # RAG — Fetch Real Papers
    papers = fetch_papers(topic)

    if not papers:
        print("⚠️  No papers found. Try a different topic.")
        return

    # Agent 1 — Literature Review
    summary = literature_agent(topic, field_data, papers)

    # Agent 2 — Critical Analysis
    critique = critic_agent(topic, field_data, papers, summary)

    # Agent 3 — Debate
    debate = debate_agent(topic, field_data, papers, summary, critique)

    # Agent 4 — Hypothesis
    hypotheses = hypothesis_agent(topic, field_data, summary, critique, debate)

    # Agent 5 — Final Report
    final_report, citations = report_agent(
        topic, field_data, papers,
        summary, critique, debate, hypotheses
    )

    # Save
    save_output(
        topic, field_data["field"],
        summary, critique, debate,
        hypotheses, final_report, citations
    )

    print("\n" + "=" * 60)
    print("✅ SwarmScholar AI Research Complete!")
    print("📂 Check outputs/ folder for your report!")
    print("=" * 60)

if __name__ == "__main__":
    main()