#!/usr/bin/python3
from file_parser import get_file_text, clean_file_contents_automatic, clean_file_contents_interactive
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_file>")
        sys.exit(1)
    path_to_file: str = sys.argv[1]
    file_contents: str = get_file_text(path_to_file)
    print("String Cleaner\n ----------- \n 1. Automatic\n 2. Interactive\n 3. Exit\n")
    string_cleaner_mode = int(input("Mode Selection: "))
    cleaned_file_contents: str = ""
    if string_cleaner_mode == 1:
        cleaned_file_contents = clean_file_contents_automatic(file_contents)
    elif string_cleaner_mode == 2:
        cleaned_file_contents = clean_file_contents_interactive(file_contents)
    elif(string_cleaner_mode == 3):
        print("Exiting Now...")
        sys.exit(1)
    else:
        raise ValueError("Invalid String Cleaner Mode Selected")
    print("---------------------------------------")
    print(cleaned_file_contents)

main()
