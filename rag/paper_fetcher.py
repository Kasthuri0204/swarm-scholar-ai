import requests
import time

SEMANTIC_SCHOLAR_URL = "https://api.semanticscholar.org/graph/v1/paper/search"

def fetch_papers(topic, max_papers=6):
    """
    Fetches real research papers from Semantic Scholar API
    Returns list of papers with title, abstract, authors, year, citations
    """
    print(f"\n📡 Fetching real papers for: {topic}")

    params = {
        "query": topic,
        "limit": max_papers,
        "fields": "title,abstract,authors,year,citationCount,externalIds"
    }

    headers = {
        "User-Agent": "SwarmScholar-Research-Tool/1.0"
    }

    try:
        response = requests.get(
            SEMANTIC_SCHOLAR_URL,
            params=params,
            headers=headers,
            timeout=15
        )

        if response.status_code == 200:
            data = response.json()
            papers = data.get("data", [])

            cleaned_papers = []
            for paper in papers:
                abstract = paper.get("abstract", "")
                if not abstract:
                    continue  # skip papers without abstract

                authors = paper.get("authors", [])
                author_names = ", ".join(
                    [a.get("name", "") for a in authors[:3]]
                )
                if len(authors) > 3:
                    author_names += " et al."

                cleaned_papers.append({
                    "title": paper.get("title", "Unknown Title"),
                    "abstract": abstract[:800],  # limit abstract length
                    "authors": author_names,
                    "year": paper.get("year", "N/A"),
                    "citations": paper.get("citationCount", 0),
                    "doi": paper.get("externalIds", {}).get("DOI", "N/A")
                })

            print(f"✅ Found {len(cleaned_papers)} papers with abstracts")
            return cleaned_papers

        elif response.status_code == 429:
            print("⚠️ Rate limited — waiting 5 seconds...")
            time.sleep(5)
            return fetch_papers(topic, max_papers)

        else:
            print(f"⚠️ API returned status {response.status_code}")
            return []

    except requests.exceptions.Timeout:
        print("⚠️ Request timed out")
        return []
    except requests.exceptions.ConnectionError:
        print("⚠️ No internet connection")
        return []
    except Exception as e:
        print(f"⚠️ Error fetching papers: {e}")
        return []


def format_papers_for_prompt(papers):
    """
    Formats paper list into a clean text block for LLM prompts
    """
    if not papers:
        return "No papers found."

    formatted = ""
    for i, paper in enumerate(papers, 1):
        formatted += f"""
PAPER {i}:
Title: {paper['title']}
Authors: {paper['authors']}
Year: {paper['year']}
Citations: {paper['citations']}
Abstract: {paper['abstract']}
DOI: {paper['doi']}
---"""
    return formatted


def format_citations(papers):
    """
    Returns a formatted citation list
    """
    if not papers:
        return "No citations available."

    citations = ""
    for i, paper in enumerate(papers, 1):
        citations += f"[{i}] {paper['authors']} ({paper['year']}). "
        citations += f"{paper['title']}."
        if paper['doi'] != "N/A":
            citations += f" DOI: {paper['doi']}"
        citations += "\n"
    return citations