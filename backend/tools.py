import os
from dotenv import load_dotenv
from langchain_core.tools import tool
import smartsheet


load_dotenv()
api_key = os.getenv("SMARTSHEET_API_KEY")


# Initialize Smartsheet client
client = smartsheet.Smartsheet(api_key)


@tool
def update_cell(sheet_id: int, row_id: int, column_id: int, value: str) -> smartsheet.models.Cell:
    """Update a cell in a Smartsheet sheet."""
    sheet = client.Sheets.get_sheet(sheet_id)
    row = sheet.get_row(row_id)
    cell = row.get_column(column_id)
    cell.value = value
    updated_cell = client.Sheets.update_rows(sheet_id, [row])
    return updated_cell


@tool
def get_cell_from_id(sheet_id: int, row_id: int, column_id: int) -> smartsheet.models.Cell:
    """Get a cell from a Smartsheet sheet by row ID and column ID."""
    sheet = client.Sheets.get_sheet(sheet_id)
    row = sheet.get_row(row_id)
    return row.cells[column_id]


@tool
def edit_row(sheet_id: int, row_id: int, data: dict) -> smartsheet.models.Row:
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
def get_row(sheet_id: int, row_id: int) -> smartsheet.models.Row:
    """Get a row from a Smartsheet sheet by ID."""
    sheet = client.Sheets.get_sheet(sheet_id)
    return sheet.get_row(row_id)


@tool
def get_row_by_value(sheet_id: int, value: str) -> smartsheet.models.Row:
    """Get a row from a Smartsheet sheet by the value in the first column."""
    sheet = client.Sheets.get_sheet(sheet_id)
    for row in sheet.rows:
        for cell in row.cells:
            if cell.value == value:
                return row
    raise ValueError(f"Row with value '{value}' not found.")


@tool
def edit_column(sheet_id: int, column_id: int, title: str, type: str) -> smartsheet.models.Column:
    """Edit a column in a Smartsheet sheet."""
    sheet = client.Sheets.get_sheet(sheet_id)
    column = sheet.get_column(column_id)
    column.title = title
    column.type = type
    updated_column = client.Sheets.update_column(sheet_id, column)
    return updated_column


@tool
def add_column(sheet_id: int, title: str, type: str) -> smartsheet.models.Column:
    """Add a new column to a Smartsheet sheet."""
    sheet = client.Sheets.get_sheet(sheet_id)
    new_column = smartsheet.models.Column({
        'title': title,
        'type': type,
        'index': len(sheet.columns)
    })
    added_column = sheet.add_columns([new_column])
    return added_column


@tool
def delete_column(sheet_id: int, column_id: int) -> None:
    """Delete a column from a Smartsheet sheet."""
    client.Sheets.delete_column(sheet_id, column_id)


@tool
def get_column(sheet_id: int, column_id: int) -> smartsheet.models.Column:
    """Get a column from a Smartsheet sheet by ID."""
    sheet = client.Sheets.get_sheet(sheet_id)
    return sheet.get_column(column_id)


@tool
def get_column_by_name(sheet_id: int, column_name: str) -> smartsheet.models.Column:
    """Get a column from a Smartsheet sheet by name."""
    sheet = client.Sheets.get_sheet(sheet_id)
    for column in sheet.columns:
        if column.title == column_name:
            return column
    raise ValueError(f"Column '{column_name}' not found.")


@tool
def get_sheet(sheet_id: int) -> smartsheet.models.Sheet:
    """Get a Smartsheet sheet by ID."""
    return client.Sheets.get_sheet(sheet_id)


@tool
def get_sheet_by_name(sheet_name: str) -> smartsheet.models.Sheet:
    """Get a Smartsheet sheet by name."""
    sheets = client.Sheets.list_sheets(include_all=True)
    for sheet in sheets.data:
        if sheet.name == sheet_name:
            return sheet
    raise ValueError(f"Sheet '{sheet_name}' not found.")


tools = [update_cell, get_cell_from_id, edit_row, add_row, delete_row, get_row, get_row_by_value, edit_column,
         add_column, delete_column, get_column, get_column_by_name, get_sheet, get_sheet_by_name]
