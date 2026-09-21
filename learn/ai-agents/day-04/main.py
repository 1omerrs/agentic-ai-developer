"""
Day 4 — Research Assistant
LLM (beyin) + web search (tool) + agent loop
"""

from concurrent.futures import ThreadPoolExecutor, TimeoutError as FuturesTimeout
from pathlib import Path

from ddgs import DDGS
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

# .env: once day-04, yoksa repo kok
_day_dir = Path(__file__).resolve().parent
_repo_root = _day_dir.parents[2]
load_dotenv(_day_dir / ".env")
load_dotenv(_repo_root / ".env")


@tool
def web_search(query: str) -> str:
    """Search the web and return short result snippets."""

    def _run() -> str:
        with DDGS() as ddgs:
            hits = list(ddgs.text(query, max_results=3))
        if not hits:
            return "No results found."
        lines = []
        for h in hits:
            title = h.get("title", "")
            body = h.get("body", "")
            href = h.get("href", "")
            lines.append(f"- {title}: {body} ({href})")
        return "\n".join(lines)

    # Arama takilirsa agent dakikalarca beklemеsin
    with ThreadPoolExecutor(max_workers=1) as pool:
        fut = pool.submit(_run)
        try:
            return fut.result(timeout=12)
        except FuturesTimeout:
            return "Search timed out. Answer from your own knowledge."


# LLM = beyin
llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

# AGENT = beyin + el
agent = create_agent(
    model=llm,
    tools=[web_search],
    system_prompt=(
        "Sen bir research assistant'sin. "
        "Gerekirse web_search kullan. Kisa ve net cevap ver. "
        "Arama timeout olursa bildigin kadar cevapla."
    ),
)


def _to_text(content) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for part in content:
            if isinstance(part, dict) and "text" in part:
                parts.append(str(part["text"]))
            else:
                parts.append(str(part))
        return "\n".join(parts)
    return str(content)


def ask(question: str) -> str:
    result = agent.invoke({"messages": [{"role": "user", "content": question}]})
    return _to_text(result["messages"][-1].content)


if __name__ == "__main__":
    question = "LangChain'i kim olusturdu?"
    print("Soru:", question)
    print("Cevap:", ask(question))
