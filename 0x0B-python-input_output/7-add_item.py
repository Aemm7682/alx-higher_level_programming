#!/usr/bin/python3
'''a function that creates an Object from a “JSON file'''


import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
arglist = list(sys.argv[1:])
try:
    data_before = load_from_json_file("add_item.json")
except Exception:
    data_before = []
data_before.extend(arglist)
save_to_json_file(data_before, "add_item.json")
