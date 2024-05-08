from smartersheet.agent import agent_executor
import sys

# Get the argument from the user
test_type = sys.argv[1]

# Testing update_cell_from_idx, get_cell_from_idx, and get_cell_from_id
if test_type == "cell":
    agent_executor.invoke(
        {
            "input": "Update the cell in the row with row id '5724192859590532' in the column 'test2' to say 'Sam.' Then get the second cell from the row. Then get the column id of the column 'test2.' Then get the cell from the row with that column id."
        }
    )
# Testing add_row, edit_row, get_row, get_row_by_value, and delete_row
elif test_type == "row":
    agent_executor.invoke(
        {
            "input": "Add a new row to the smartsheet called 'Sample Sheet'. Then edit the row to have ascending integers in each column. Then get the row with the value 'test' in the column called 'test'. Then get the row with id '5724192859590532.' Then delete the row.",
        }
    )
# Testing add_column, get_column_by_name, get_column, edit_column, and delete_column
elif test_type == "column":
    agent_executor.invoke(
        {
            "input": "Create a new column called 'test3' in the smartsheet called 'Sample Sheet'. Then get the column called 'test2'. Then using the ID of the column, get the column with that ID. Then edit the column 'test3' to be called 'test4' and change the type of the column to a checkbox. Then delete the column called 'test4.'",
        }
    )
# Testing get_sheet and get_sheet_by_namee
elif test_type == "sheet":
    agent_executor.invoke(
        {
            "input": "Get the smartsheet called 'Sample Sheet'. Then get the sheet with ID '6853197486313348'. Then create a sheet called 'Hello World.' Then delete the sheet.",
        }
    )
else:
    print("Invalid test type. Please specify 'cell', 'row', 'column', or 'sheet'.")
