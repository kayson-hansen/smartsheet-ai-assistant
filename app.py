import os
from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_anthropic import ChatAnthropic

from tools import tools

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

llm = ChatAnthropic(model="claude-3-sonnet-20240229")

# Get the prompt to use - you can modify this!
prompt = hub.pull("hwchase17/openai-tools-agent")
prompt.pretty_print()

# Construct the tool calling agent
agent = create_tool_calling_agent(llm, tools, prompt)

# Create an agent executor by passing in the agent and tools
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

agent_executor.invoke(
    {
        "input": "Using the get_sheet_by_name tool, get the sheet called 'Sample Sheet.' Then delete the column called 'Remaining.'",
    }
)
