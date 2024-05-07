from langchain import hub
from langchain.agents import AgentExecutor, create_tool_calling_agent

# Get the prompt to use - you can modify this!
prompt = hub.pull("hwchase17/openai-tools-agent")
prompt.pretty_print()
