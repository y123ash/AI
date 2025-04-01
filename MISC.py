import os

# Extensions to include (files you write)
INCLUDE_EXTENSIONS = {'.py'}

# Auto-generated folders to skip
EXCLUDE_FOLDERS = {
    '__pycache__', '.pytest_cache', '.git', '.vscode', '.idea',
    'Lib', 'Scripts', 'Include', 'share', 'bin', 'dist', 'build'
}

# Auto-generated files to skip
EXCLUDE_FILENAMES = {'pyvenv.cfg'}

def print_manual_tree(path, depth=0):
    basename = os.path.basename(path)
    if basename in EXCLUDE_FOLDERS:
        return

    try:
        entries = os.listdir(path)
    except (PermissionError, FileNotFoundError):
        return

    entries = sorted(entries)
    for entry in entries:
        full_path = os.path.join(path, entry)

        if os.path.isdir(full_path):
            if entry not in EXCLUDE_FOLDERS:
                print("│   " * depth + f"├── {entry}/")
                print_manual_tree(full_path, depth + 1)
        else:
            ext = os.path.splitext(entry)[1]
            if entry in EXCLUDE_FILENAMES or not ext in INCLUDE_EXTENSIONS:
                continue
            print("│   " * depth + f"├── {entry}")

# Set your project path here
project_path = r"D:\C_OVERLOAD\AGENT_TURACOZ"
print_manual_tree(project_path)