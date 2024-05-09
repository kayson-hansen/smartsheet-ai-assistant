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
    """Update a cell in a Smartsheet sheet using the row id and column id."""
    # Build new cell value
    new_cell = smartsheet.models.Cell()
    new_cell.column_id = column_id
    new_cell.value = value
    new_cell.strict = False

    # Build the row to update
    new_row = smartsheet.models.Row()
    new_row.id = row_id
    new_row.cells.append(new_cell)

    # Update rows
    updated_row = client.Sheets.update_rows(sheet_id, [new_row])
    return updated_row


@tool
def get_cell_from_idx(sheet_id: int, row_id: int, row_idx: int) -> smartsheet.models.Cell:
    """Get a cell from a Smartsheet sheet by row id and row index (row_idx represents
    which column the cell is in, assuming the columns are 0-indexed starting from the leftmost column)."""
    sheet = client.Sheets.get_sheet(sheet_id)
    row = sheet.get_row(row_id)
    return row.cells[row_idx]


@tool
def get_cell_from_id(sheet_id: int, row_id: int, column_id: int) -> smartsheet.models.Cell:
    """Get a cell from a Smartsheet sheet by row ID and column ID."""
    sheet = client.Sheets.get_sheet(sheet_id)
    row = sheet.get_row(row_id)
    for cell in row.cells:
        if cell.column_id == column_id:
            return cell.value


@tool
def edit_row(sheet_id: int, row_id: int, data: dict) -> smartsheet.models.Row:
    """Edit a row in a Smartsheet sheet. data is a dict with the column ID as the key and the new
    cell value as the value."""
    # Create a new row
    new_row = smartsheet.models.Row()
    new_row.id = row_id

    # Add cells to the row
    for column_id, value in data.items():
        cell = smartsheet.models.Cell()
        cell.column_id = int(column_id)
        cell.value = value
        new_row.cells.append(cell)

    # Update the row
    updated_row = client.Sheets.update_rows(sheet_id, [new_row])
    return updated_row


@tool
def add_row(sheet_id: int, data: dict) -> dict:
    """Add a new row to a Smartsheet sheet."""
    new_row = smartsheet.models.Row()
    new_row.to_top = True
    for column_id, value in data.items():
        new_row.set_column(column_id, value)
    added_row = client.Sheets.add_rows(sheet_id, [new_row])
    return added_row


@tool
def delete_rows(sheet_id: int, row_ids: list[int]) -> None:
    """Deletes the given rows from a Smartsheet sheet."""
    client.Sheets.delete_rows(sheet_id, row_ids)


@tool
def get_row(sheet_id: int, row_id: int) -> smartsheet.models.Row:
    """Get a row from a Smartsheet sheet by ID."""
    sheet = client.Sheets.get_sheet(sheet_id)
    return sheet.get_row(row_id)


@tool
def edit_column(sheet_id: int, column_id: int, title: str, type: str) -> smartsheet.models.Column:
    """Edit a column in a Smartsheet sheet."""
    # Specify column properties
    column_spec = smartsheet.models.Column({
        'title': title,
        'type': type,
        'index': 0
    })

    # Update column
    response = client.Sheets.update_column(sheet_id, column_id, column_spec)
    return response.result


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
def get_columns(sheet_id: int) -> list[smartsheet.models.Column]:
    """Get all columns from a Smartsheet sheet."""
    response = client.Sheets.get_columns(sheet_id, include_all=True)
    columns = response.data
    return columns


@tool
def get_column_by_name(sheet_id: int, column_name: str) -> smartsheet.models.Column:
    """Get a column from a Smartsheet sheet by name."""
    response = client.Sheets.get_columns(sheet_id, include_all=True)
    columns = response.data
    for column in columns:
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


@tool
def create_sheet(name: str, folder_id: int = None, template_id: int = None) -> smartsheet.models.Sheet:
    """Create a new Smartsheet sheet."""
    sheet_spec = smartsheet.models.Sheet({
        'name': name,
        'columns': [{
            'title': 'Favorite',
            'type': 'CHECKBOX',
            'symbol': 'STAR'
        }, {
            'title': 'Primary Column',
            'primary': True,
            'type': 'TEXT_NUMBER'
        }
        ]
    })

    if folder_id is not None and template_id is None:
        # Case 1: Create sheet in folder
        response = client.Folders.create_sheet_in_folder(folder_id, sheet_spec)
        new_sheet = response.result
    elif folder_id is not None and template_id is not None:
        # Case 2: Create sheet in folder from template
        response = client.Folders.create_sheet_in_folder_from_template(
            folder_id,
            smartsheet.models.Sheet({
                'name': 'newsheet',
                'from_id': template_id
            })
        )
    elif folder_id is None and template_id is not None:
        # Case 3: Create sheet from template
        response = client.Home.create_sheet_from_template(
            smartsheet.models.Sheet({
                'name': 'newsheet',
                'from_id': template_id
            })
        )
        new_sheet = response.result
    else:
        # Case 4: Create new sheet
        response = client.Home.create_sheet(sheet_spec)
        new_sheet = response.result
    return new_sheet


@tool
def delete_sheet(sheet_id: int) -> None:
    """Delete a Smartsheet sheet by ID."""
    client.Sheets.delete_sheet(sheet_id)


tools = [update_cell, get_cell_from_idx, get_cell_from_id, edit_row, add_row, delete_rows, get_row, edit_column,
         add_column, delete_column, get_column, get_column_by_name, get_sheet, get_sheet_by_name, create_sheet,
         delete_sheet]
