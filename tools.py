import os
from dotenv import load_dotenv
from langchain_core.tools import tool
import smartsheet


load_dotenv()
api_key = os.getenv("SMARTSHEET_API_KEY")


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


@tool
def get_sheet(sheet_id: int) -> smartsheet.models.Sheet:
    """Get a Smartsheet sheet by ID."""
    return client.Sheets.get_sheet(sheet_id)


@tool
def get_row(sheet_id: int, row_id: int) -> smartsheet.models.Row:
    """Get a row from a Smartsheet sheet by ID."""
    sheet = client.Sheets.get_sheet(sheet_id)
    return sheet.get_row(row_id)


@tool
def get_column(sheet_id: int, column_id: int) -> smartsheet.models.Column:
    """Get a column from a Smartsheet sheet by ID."""
    sheet = client.Sheets.get_sheet(sheet_id)
    return sheet.get_column(column_id)


@tool
def update_cell(sheet_id: int, row_id: int, column_id: int, value: str) -> smartsheet.models.Cell:
    """Update the value of a cell in a Smartsheet sheet."""
    sheet = client.Sheets.get_sheet(sheet_id)
    cell = sheet.get_cell(row_id, column_id)
    cell.value = value
    updated_cell = client.Sheets.update_cells(sheet_id, [cell])
    return updated_cell


@tool
def add_column(sheet_id: int, title: str, type: str) -> smartsheet.models.Column:
    """Add a new column to a Smartsheet sheet."""
    sheet = client.Sheets.get_sheet(sheet_id)
    new_column = smartsheet.models.Column({
        'title': title,
        'type': type
    })
    added_column = client.Sheets.add_columns(sheet_id, [new_column])
    return added_column


@tool
def delete_column(sheet_id: int, column_id: int) -> None:
    """Delete a column from a Smartsheet sheet."""
    client.Sheets.delete_column(sheet_id, column_id)


@tool
def get_sheet_by_name(sheet_name: str) -> smartsheet.models.Sheet:
    """Get a Smartsheet sheet by name."""
    sheets = client.Sheets.list_sheets(include_all=True)
    for sheet in sheets.data:
        if sheet.name == sheet_name:
            return sheet
    raise ValueError(f"Sheet '{sheet_name}' not found.")


@tool
def get_column_by_name(sheet_id: int, column_name: str) -> smartsheet.models.Column:
    """Get a column from a Smartsheet sheet by name."""
    sheet = client.Sheets.get_sheet(sheet_id)
    for column in sheet.columns:
        if column.title == column_name:
            return column
    raise ValueError(f"Column '{column_name}' not found.")


tools = [edit_row, add_row, delete_row, get_sheet, get_row,
         get_column, update_cell, add_column, delete_column,
         get_sheet_by_name, get_column_by_name]
