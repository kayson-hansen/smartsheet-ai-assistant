from backend.agent import agent_executor
import sys
# Get the argument from the user
test_type = sys.argv[1]

# Testing update_cell and get_cell_from_id
if test_type == "cell":
    agent_executor.invoke(
        {
            "input": "Get the column with name 'test2.' Get the ID from that column, then \
                get the cell with row ID '5724192859590532' and the column ID from before.'"
        }
    )
# Testing add_row, edit_row, get_row, get_row_by_value, and delete_rowow
elif test_type == "row":
    agent_executor.invoke(
        {
            "input": "Add a new row to the smartsheet called 'Sample Sheet'. Then edit the row to have the \
                value 'test' in the column called 'test'. Then get the row with the value 'test' in the column \
                called 'test'. Then get the row with id '5724192859590532.' Then delete the row with \
                the value 'test' in the column called 'test'.",
        }
    )
# Testing add_column, get_column_by_name, get_column, edit_column, and delete_columnmn
# Also tests get_sheet,
elif test_type == "column":
    agent_executor.invoke(
        {
            "input": "Create a new column called 'test2' in the smartsheet called 'Sample Sheet. Then \
                get the column called 'test2'. Then using the ID of the column, get the column with that \
                ID. Then edit the column 'test2' to have ascending integers in each of the cells. Then \
                delete the column called 'test2'.",
        }
    )
# Testing get_sheet and get_sheet_by_namee
elif test_type == "sheet":
    agent_executor.invoke(
        {
            "input": "Get the smartsheet called 'Sample Sheet'. Then get the sheet with ID \
                '6853197486313348'.",
        }
    )
else:
    print("Invalid test type. Please specify 'cell', 'row', 'column', or 'sheet'.")
