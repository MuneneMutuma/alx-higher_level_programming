#!/usr/bin/python3
import sys
import json

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


data = sys.argv[1:]
tmp = load_from_json_file("add_item.json")
tmp.extend(data)
save_to_json_file(tmp, "add_item.json")
