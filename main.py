#!/usr/bin/python3
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

def get_file_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def is_field_header(current_value: str, next_value: str, previous_value: str) -> tuple[bool, bool, bool]:
    # First value of Tuple is for "Beginning of Header. Do not have a leading space." Second value "Middle of the header. Have a leading and trailing space."
    # Last value is "End of the header. Have a leading space and a line return at the end"
    if current_value.isupper() == False:
        return (False,False,False)
    elif current_value.isupper() and previous_value.isupper() and next_value.isupper():
        return(False, True, False)
    elif previous_value.isupper() and current_value.isupper() and next_value.isupper() == False:
        return(False, False, True)
    elif previous_value.isupper() == False and current_value.isupper() and next_value.isupper():
        return(True, False, False)
    elif previous_value.isupper() == False and current_value.isupper() and next_value.isupper() == False:
        return(True, False, True)
    else:
        return(False,False,False)

def check_for_hyphen_split(current_val: str) -> str:
    if current_val.endswith("-"):
        return current_val.replace("-", "")
    else:
        return current_val



def clean_file_contents_automatic(file_contents: str) -> str:
    split_file_contents: list[str] = file_contents.split("\n")
    output_file_contents: list[str] = []
    for i in range(len(split_file_contents) - 1):
        if(i > 0):
            prev_val = split_file_contents[i-1]
        else:
            prev_val = ""
        if i == len(split_file_contents):
            next_val = ""
        else:
            next_val = split_file_contents[i +1]
        current_val: str = split_file_contents[i]
        header_status: tuple[bool,bool,bool] = is_field_header(current_val, next_val, prev_val)
        current_val = check_for_hyphen_split(current_val)
        print(f"Previous:{prev_val}\nCurrent:{current_val}\nNext:{next_val}\nHeader Results:{header_status}\n -------------")

        if header_status == (True, False, True):
            output_file_contents.append(current_val + "\n")
        elif header_status == (True, False, False):
            output_file_contents.append("\n" + current_val.replace("\n", " "))
        elif header_status == (False, True, False):
            output_file_contents.append(" " + current_val.replace("\n", " "))
        elif header_status == (False, False, True):
            output_file_contents.append(" " + current_val + "\n")
        else:
            output_file_contents.append(current_val.replace("\n", " ") + " ")
    return "".join(output_file_contents).replace("•", "- ")

def clean_file_contents_interactive(file_contents: str) -> str:
    split_file_contents: list[str] = file_contents.split("\n")
    output_file_contents: list[str] = []
    bullet_point_decision: str = ""
    for i in range(len(split_file_contents) - 1):
        if(i > 0):
            prev_val = split_file_contents[i-1]
        else:
            prev_val = ""
        if i == len(split_file_contents):
            next_val = ""
        else:
            next_val = split_file_contents[i +1]
        current_val: str = split_file_contents[i]
        header_status: tuple[bool,bool,bool] = is_field_header(current_val, next_val, prev_val)
        current_val = check_for_hyphen_split(current_val)
        print(f"Previous:{prev_val}\nCurrent:{current_val}\nNext:{next_val}\nHeader Results:{header_status}\n -------------")

        if header_status == (True, False, True):
            output_file_contents.append(current_val + "\n")
        elif header_status == (True, False, False):
            output_file_contents.append("\n" + current_val.replace("\n", " "))
        elif header_status == (False, True, False):
            output_file_contents.append(" " + current_val.replace("\n", " "))
        elif header_status == (False, False, True):
            output_file_contents.append(" " + current_val + "\n")
        elif current_val.startswith("•") == False and next_val.startswith("•"):
            output_file_contents.append(current_val + "\n")
        elif(bullet_point_decision == "C"):
            bullet_point_decision = input(f"Current line: {current_val}\n Next line: {next_val}\n (N)ew Line/(C)ontinue Line? ").upper()
            if bullet_point_decision == "N":
                output_file_contents.append(current_val + "\n")
            elif bullet_point_decision == "C":
                output_file_contents.append(current_val.replace("\n", " "))
            else:
                print("Invalid option selected. Defaulting to Continue Line.")
                output_file_contents.append(current_val.replace("\n", " "))
        elif(current_val[0] == "•" and next_val[0] == "•"):
            output_file_contents.append(current_val + "\n")
        elif(current_val[0] == "•" and next_val[0] != "•"):
            if next_val == "" or next_val == None:
                output_file_contents.append(current_val + "\n")
                continue
            bullet_point_decision = input(f"Current line: {current_val}\n Next line: {next_val}\n (N)ew Line/(C)ontinue Line? ").upper()
            if bullet_point_decision == "N":
                output_file_contents.append(current_val + "\n")
            elif bullet_point_decision == "C":
                output_file_contents.append(current_val.replace("\n", " "))
            else:
                print("Invalid option selected. Defaulting to Continue Line.")
                output_file_contents.append(current_val.replace("\n", " "))
        else:
            output_file_contents.append(current_val.replace("\n", " ") + " ")
    return "".join(output_file_contents).replace("•", "- ")

main()
