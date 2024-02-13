from pathlib import Path
import os
import shutil


def get_file_count(directory, prefix):
    count = 0
    for filename in os.listdir(directory):
        if filename.startswith(prefix) and filename.endswith(".py"):
            count += 1
    return count


def move_files(source_directory, destination_directory, prefix):
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    for filename in os.listdir(source_directory):
        if filename.startswith(prefix) and filename.endswith(".py"):
            source_file = os.path.join(source_directory, filename)
            dest_file = os.path.join(destination_directory, filename)
            shutil.move(source_file, dest_file)
            print(f"Moved {filename} to {destination_directory}")


def main():
    source_directory = Path("../pyUdemy")

    py_regex_count = get_file_count(source_directory, "pyRegex")
    py_file_count = get_file_count(source_directory, "pyFile")
    py_excel_count = get_file_count(source_directory, "pyExcel")

    print(f"Found {py_regex_count} pyRegex files\n")
    print(f"Found {py_file_count} pyFile files\n")
    print(f"Found {py_excel_count} pyFile files\n")

    move_files(source_directory, source_directory / "pyRegex", "pyRegex")
    move_files(source_directory, source_directory / "pyFile", "pyFile")
    move_files(source_directory, source_directory / "pyExcel", "pyExcel")



if __name__ == "__main__":
    main()
