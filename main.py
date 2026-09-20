#!/usr/bin/python3
import sys
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_file>")
        sys.exit(1)
    path_to_file: str = sys.argv[1]
    file_contents: str = get_file_text(path_to_file)
    cleaned_file_contents: str = clean_file_contents(file_contents)
    print(cleaned_file_contents)

def get_file_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def clean_file_contents(file_contents: str) -> str:
    return file_contents.replace("\n", " ").replace("- ", "")

main()
