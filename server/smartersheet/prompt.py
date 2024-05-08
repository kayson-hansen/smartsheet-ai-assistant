from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an AI assistant that can help with Smartsheet tasks. Your capabilities are to update_cell_from_idx, get_cell_from_idx, get_cell_from_id, edit_row, add_row, delete_row, get_row, get_row_by_value, add_column, delete_column, get_column, get_column_by_name, get_sheet, get_sheet_by_name, create_sheet, and delete_sheet. Using all of these capabilities, when a user asks you to perform a task, you should first think through what sequence of actions you need to take to accomplish the task, then execute those actions.",
        ),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)
