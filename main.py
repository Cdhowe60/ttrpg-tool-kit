#!/usr/bin/python3
import sys
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_file>")
        sys.exit(1)
    path_to_file: str = sys.argv[1]
    file_contents: str = get_file_text(path_to_file)
    cleaned_file_contents: str = clean_file_contents(file_contents)
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


def clean_file_contents(file_contents: str) -> str:
    split_file_contents: list[str] = file_contents.split("\n")
    output_file_contents: list[str] = []
    continue_bullet_point: bool = False
    for i in range(len(split_file_contents) - 1):
        if(i > 0):
            prev_val = split_file_contents[i-1]
        else:
            prev_val = ""
        if i == len(split_file_contents):
            next_val = ""
        else:
            next_val = split_file_contents[i +1]
        current_val = split_file_contents[i]
        header_status: tuple[bool,bool,bool] = is_field_header(current_val, next_val, prev_val)
        print(f"Current Val: {current_val}")
        print(f"Next Val: {next_val}")
        print(f"Previous Val: {prev_val}")
        print(f"Is field header result {header_status}")
        print("-")

        if header_status == (True, False, True):
            output_file_contents.append(current_val + "\n")
        elif header_status == (True, False, False):
            output_file_contents.append(current_val.replace("\n", " "))
        elif header_status == (False, True, False):
            output_file_contents.append(" " + current_val.replace("\n", " "))
        elif header_status == (False, False, True):
            output_file_contents.append(" " + current_val + "\n")
        elif(current_val[-1] == "-"):
            print(5)
            output_file_contents.append(current_val.replace("-", ""))
        elif(current_val[0] == "•" and next_val[0] == "•"):
            print(6)
            #continue_bullet_point = False
            output_file_contents.append(current_val + "\n")
        elif(current_val[0] == "•" and next_val[0] != "•"):
            print(7)
            output_file_contents.append(current_val.replace("\n", "") + " ")
        else:
            print(8)
            output_file_contents.append(current_val.replace("\n", " ") + " ")

    return "".join(output_file_contents)

main()
