# File Renaming Script

This script automatically renames `.IGS` and `.pdf` files based on matching data from an Excel spreadsheet.

## Overview

The script matches filenames against a list of manufacturing part numbers (MFG PN) and renames them to their corresponding engineering numbers (EN#), while preserving the original file extension.

## Requirements

- Python 3.x
- pandas library
- openpyxl library (for Excel file support)

Install dependencies:
```bash
pip install pandas openpyxl
```

## File Structure

- `rename.py` - Main script
- `names.xlsx` - Excel file containing mapping data
- `IGS/` - Folder containing files to be renamed
- `file_renaming.log` - Log file generated during execution

## Excel File Format

The Excel file (`names.xlsx`) must contain the following columns:
- **EN#** - Engineering number (new filename)
- **MFG PN** - Manufacturing part number (used to match existing filenames)

Example:
| EN# | MFG PN |
|-----|---------|
| 601-1-20769 | ABC123 |
| 601-2-17246 | XYZ789 |

## How It Works

1. Loads the Excel file containing the EN# to MFG PN mapping
2. Scans the `IGS/` folder for `.IGS` and `.pdf` files
3. For each file, searches for a matching MFG PN in the filename
4. If a match is found, renames the file to `{EN#}.{original_extension}`
5. Logs all actions (successful renames, no matches, errors) to `file_renaming.log`

## Usage

Run the script from the command line:
```bash
python rename.py
```

## Example

**Before:**
- `ABC123-datasheet.IGS`
- `XYZ789-drawing.pdf`

**After:**
- `601-1-20769.IGS`
- `601-2-17246.pdf`

## Configuration

Edit these paths in the script if needed:
```python
folder_path = "C:/Users/Panda/Documents/VD/IGS"  # Folder with files to rename
excel_path = "C:/Users/Panda/Documents/VD/names.xlsx"  # Mapping file
```

## Logging

All operations are logged to `file_renaming.log`:
- **INFO** - Successful renames
- **WARNING** - Files with no matching MFG PN
- **ERROR** - Any errors encountered

## Notes

- The script performs case-insensitive matching
- It looks for the MFG PN as a substring within the filename
- Original file extensions are preserved (`.IGS` stays `.IGS`, `.pdf` stays `.pdf`)
- Files without matches are left unchanged
