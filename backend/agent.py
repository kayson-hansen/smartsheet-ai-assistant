import os
from dotenv import load_dotenv
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_anthropic import ChatAnthropic

from tools import tools
from prompt import prompt

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

llm = ChatAnthropic(model="claude-3-sonnet-20240229")

# Construct the tool calling agent
agent = create_tool_calling_agent(llm, tools, prompt)

# Create an agent executor by passing in the agent and tools
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
