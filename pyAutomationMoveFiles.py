from pathlib import Path
import os
import shutil

def get_file_count(directory, prefix):
    count = 0
    for filename in os.listdir(directory):
        if filename.startswith(prefix) and filename.endswith(".py"):
            count += 1
    return count

def move_files(sourceDirectory, destinationDirectory, prefix):
    if not os.path.exists(destinationDirectory):
        os.makedirs(destinationDirectory)
    for filename in os.listdir(sourceDirectory):
        if filename.startswith(prefix) and filename.endswith(".py"):
            source_file = os.path.join(sourceDirectory, filename)
            dest_file = os.path.join(destinationDirectory, filename)
            shutil.move(source_file, dest_file)
            print(f"Moved {filename} to {destinationDirectory}")

def main():
    sourceDirectory = Path("c:/Users/admin/Desktop/python_Antonio")

    pyRegex_count = get_file_count(sourceDirectory, "pyRegex")
    pyFile_count = get_file_count(sourceDirectory, "pyFile")

    print(f"Found {pyRegex_count} pyRegex files\n")
    print(f"Found {pyFile_count} pyFile files\n")

    move_files(sourceDirectory, sourceDirectory / "pyRegex", "pyRegex")
    move_files(sourceDirectory, sourceDirectory / "pyFile", "pyFile")

if __name__ == "__main__":
    main()