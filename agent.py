from memory_manager import remember_user
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain_community.tools import DuckDuckGoSearchRun

llm = ChatOllama(
    model="qwen3:8b",
    temperature=0
)

search = DuckDuckGoSearchRun()

tools = [search]

agent = create_agent(
    model=llm,
    tools=tools
)

def get_response(question):

    remember_user(question)

    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ]
        }
    )

    return response["messages"][-1].content