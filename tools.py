import os
from dotenv import load_dotenv
from langchain_core.tools import tool
import smartsheet


load_dotenv()
api_key = os.getenv("SMARTSHEET_API_KEY")


@tool
def multiply(first_int: int, second_int: int) -> int:
    """Multiply two integers together."""
    return first_int * second_int


@tool
def add(first_int: int, second_int: int) -> int:
    "Add two integers."
    return first_int + second_int


@tool
def exponentiate(base: int, exponent: int) -> int:
    "Exponentiate the base to the exponent power."
    return base**exponent


# Initialize Smartsheet client
client = smartsheet.Smartsheet(api_key)


@tool
def edit_row(sheet_id: int, row_id: int, data: dict) -> dict:
    """Edit a row in a Smartsheet sheet."""
    sheet = client.Sheets.get_sheet(sheet_id)
    row = sheet.get_row(row_id)
    for column_id, value in data.items():
        row.set_column(column_id, value)
    updated_row = client.Sheets.update_rows(sheet_id, [row])
    return updated_row


@tool
def add_row(sheet_id: int, data: dict) -> dict:
    """Add a new row to a Smartsheet sheet."""
    sheet = client.Sheets.get_sheet(sheet_id)
    new_row = smartsheet.models.Row()
    for column_id, value in data.items():
        new_row.set_column(column_id, value)
    added_row = client.Sheets.add_rows(sheet_id, [new_row])
    return added_row


@tool
def delete_row(sheet_id: int, row_id: int) -> None:
    """Delete a row from a Smartsheet sheet."""
    client.Sheets.delete_row(sheet_id, row_id)
