"""Day 7 — short-term memory with thread_id."""

from pathlib import Path

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import MemorySaver

_day_dir = Path(__file__).resolve().parent
_repo_root = _day_dir.parents[2]
load_dotenv(_day_dir / ".env")
load_dotenv(_repo_root / ".env")

checkpointer = MemorySaver()
llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

agent = create_agent(
    model=llm,
    tools=[],
    system_prompt=(
        "Sen yardimci bir asistansin. "
        "Bu sohbette kullanicinin soylediklerini hatirla. "
        "Kisa cevap ver."
    ),
    checkpointer=checkpointer,
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


def ask(question: str, thread_id: str) -> str:
    """Ask the agent; same thread_id shares short-term memory."""
    config = {"configurable": {"thread_id": thread_id}}
    result = agent.invoke(
        {"messages": [{"role": "user", "content": question}]},
        config=config,
    )
    return _to_text(result["messages"][-1].content)


if __name__ == "__main__":
    print("--- thread-1 ---")
    print("1)", ask("Merhaba, benim adim Omer.", "thread-1"))
    print("2)", ask("Benim adim ne?", "thread-1"))
    print("3)", ask("Favori rengim mavi.", "thread-1"))
    print("4)", ask("Favori rengim ne?", "thread-1"))

    print("\n--- thread-2 (yeni sohbet) ---")
    print("1)", ask("Benim adim ne?", "thread-2"))
    print("2)", ask("Favori rengim ne?", "thread-2"))
