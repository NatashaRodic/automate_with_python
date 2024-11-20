from pathlib import Path
import os

# 1. Create a directory and a nested folder structure
base_dir = Path("practice_files")
nested_dir = base_dir / "nested" / "folder1"
nested_dir.mkdir(parents=True, exist_ok=True)

# 2. Create a text file inside the nested folder and write some content
file_path = nested_dir / "example.txt"
with open(file_path, 'w') as file:
    file.write("Hello, this is a test file.\n")
    file.write("This file is created to practice file handling.\n")

# 3. Read and print the contents of the file
with open(file_path, 'r') as file:
    print("File contents:")
    print(file.read())

# 4. Append some additional content to the file
with open(file_path, 'a') as file:
    file.write("Appending a new line to the file.\n")

# 5. Read the updated contents of the file
with open(file_path, 'r') as file:
    print("Updated file contents:")
    print(file.read())

# 6. List all files in the nested folder
print("\nFiles in nested folder:")
for item in nested_dir.iterdir():
    if item.is_file():
        print(f"- {item.name}")

# 7. Rename the file
new_file_path = nested_dir / "renamed_example.txt"
os.rename(file_path, new_file_path)
print(f"\nFile renamed to: {new_file_path.name}")

# 8. Move the file to the base directory
moved_file_path = base_dir / new_file_path.name
os.replace(new_file_path, moved_file_path)
print(f"File moved to: {moved_file_path}")

# 9. Handle file reading with exception handling
try:
    with open("nonexistent.txt", 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("\nAttempted to read a nonexistent file. FileNotFoundError caught.")

# 10. Delete the moved file and the directories
if moved_file_path.exists():
    moved_file_path.unlink()
    print(f"\nFile {moved_file_path.name} deleted.")

# Clean up the directories and their contents
def remove_dir_and_contents(directory: Path):
    if directory.exists() and directory.is_dir():
        for item in directory.iterdir():
            if item.is_dir():
                remove_dir_and_contents(item)  # Recursively delete subdirectories
            else:
                item.unlink()  # Delete files
        directory.rmdir()  # Remove the now-empty directory

# Call the cleanup function
remove_dir_and_contents(base_dir)
print("All directories and their contents cleaned up.")

