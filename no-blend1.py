import os, sys

def format_size(size_in_bytes):
    """ Convert size from bytes to MB or KB. """
    if size_in_bytes < 1024:  # Less than 1KB
        return f"{size_in_bytes} bytes"
    elif size_in_bytes < (1024 * 1024):  # Less than 1MB
        return f"{size_in_bytes / 1024:.2f} KB"
    else:
        return f"{size_in_bytes / (1024 * 1024):.2f} MB"

def walk_and_print(path):
    found_files = []  # List to store found files
    total_size = 0    # Variable to store the total size of all files

    for dirpath, dirnames, filenames in os.walk(path):
        print(f"Scanning: {dirpath}", end='\r', flush=True)
        for filename in filenames:
            if filename.endswith('.blend1'):
                file_path = os.path.join(dirpath, filename)
                file_size = os.path.getsize(file_path)
                found_files.append((file_path, file_size))
                total_size += file_size

    print("")
    print("\n✨ Finished scanning.                                  ")
    print(f"🔍 {len(found_files)} files found:")

    # Table header
    print("")
    print(f"{'File Path':<80} {'Size':>10}")
    print("-" * 91)

    for file_path, file_size in found_files:
        formatted_size = format_size(file_size)
        print(f"{file_path:<80} {formatted_size:>10}")

    print("-" * 91)
    print(f"{'Total size of files:':<80} {format_size(total_size):>10}")

    # Ask for user confirmation to delete files
    if found_files:
        print(f"\n🚨 {bold('Deleting files using this method cannot be undone. Make sure you have made backups of the files before continuing.')}")
        user_input = input("🤔 Do you want to delete all listed '.blend1' files? (Y/N): ").strip().upper()
        if user_input == 'Y':
            for file_path, _ in found_files:
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")
            print("All listed files have been deleted.")
        else:
            print("File deletion cancelled.")

def bold(text):
    return f"\033[1m{text}\033[0m"

## Begin interface...
print(f"{bold('no-blend1 is provided as is. no guarantee. no promises. run this code at your own risk.')}")
print("Press enter to start...")
sys.stdin.readline()
walk_and_print('.')  # current directory
