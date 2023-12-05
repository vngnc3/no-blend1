# no-blend1: Clean up .blend1 files 🕵️‍♂️🗑️

This Python script is designed to search through directories for `.blend1` files, list them in a formatted table along with their sizes, and optionally delete them upon user confirmation.

## Features

- 🔍 Scans the current directory and all subdirectories for `.blend1` files.
- 📊 Displays a neatly formatted table showing the file path and size of each `.blend1` file found.
- 📏 Sizes are shown in bytes, KB, or MB as appropriate.
- 🗑️ Option to delete all found `.blend1` files after confirmation from the user.

## Usage

1. Put the `no-blend1.py` script in the directory you want to scan.
2. Run the script using terminal or shell of your choice:  
```bash
python no-blend1.py
```
3. The script will start scanning and display found files in a table format.
4. After listing files, it will ask if you want to delete them:
   - Type `Y` and press Enter to confirm deletion.
   - Type `N` or any other key and press Enter to cancel deletion.

## Warning ⚠️

**Deleting files using this script cannot be undone.**  
Make sure you have made backups of the files before proceeding with deletion.

## Contribution

Feel free to contribute to this script by submitting pull requests or suggesting improvements.

## License

This script is provided "as is", with no guarantees or promises. Use it at your own risk.