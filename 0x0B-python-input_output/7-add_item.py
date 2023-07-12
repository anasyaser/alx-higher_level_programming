#!/usr/bin/python3
"""
Add all script argument to list and save to file
"""
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def add_item(file_name, args):
    """Add script arguments to list and save them as json file objectooooj"""
    try:
        file_lst = load_from_json_file(file_name)
        file_lst += args
        save_to_json_file(file_lst, file_name)
    except Exception:
        save_to_json_file(args, file_name)


if __name__ == "__main__":
    add_item("add_item.json", sys.argv[1:])
