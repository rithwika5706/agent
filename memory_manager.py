from langchain_ollama import ChatOllama
from memory import save_memory


llm = ChatOllama(
    model="qwen3:8b",
    temperature=0
)


def remember_user(message):

    prompt = f"""
You are a memory manager.

Analyze this user message:

"{message}"

Decide whether this is useful long-term information.

Save only:
- Name
- Education
- Job
- Skills
- Preferences
- Goals
- Important personal facts

If useful, return only the memory text.
If not useful, return:
NO_MEMORY
"""

    result = llm.invoke(prompt)

    memory = result.content.strip()


    if memory != "NO_MEMORY":
        save_memory(memory)
