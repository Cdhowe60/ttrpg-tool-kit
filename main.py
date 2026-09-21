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
    split_file_contents: list[str] = file_contents.split("\n")
    output_file_contents: list[str] = []
    for i in range(len(split_file_contents) - 1):
        if(i > 0):
            prev_val = split_file_contents[i-1]
        else:
            prev_val = ""
        current_val = split_file_contents[i]
        print(f"Current Val: {current_val}")
        next_val = split_file_contents[i +1]
        print(f"Next Val: {next_val}")


        if(i == 0 and next_val.isupper() == True):
            print(1)
            output_file_contents.append(current_val.replace("\n", " "))
        elif(i == 0):
            print(2)
            output_file_contents.append(current_val + "\n")
        elif(current_val.isupper() == True and next_val.isupper() == True and prev_val.isupper() == False):
            print(3)
            output_file_contents.append("\n" + current_val.replace("\n", " ") + " ")
        elif(current_val.isupper() == True and next_val.isupper() == True):
            print(3.5)
            output_file_contents.append(current_val.replace("\n", " ") + " ")
        elif(current_val.isupper() == True and next_val.isupper() == False):
            print(4)
            output_file_contents.append(current_val + "\n")
        elif(current_val[-1] == "-"):
            print(5)
            output_file_contents.append(current_val.replace("-", ""))
        elif(current_val[0] == "•" and next_val[0] == "•"):
            print(6)
            output_file_contents.append(current_val + "\n")
        elif(current_val[0] == "•" and next_val[0] != "•"):
            print(7)
            output_file_contents.append(current_val.replace("\n", "") + " ")
        else:
            print(8)
            output_file_contents.append(current_val.replace("\n", " ") + " ")

    return "".join(output_file_contents)

main()
