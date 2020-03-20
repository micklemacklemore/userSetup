import os
import json

# json_string = '''
# {
#   "00_Pipeline" : "",
#   "Project_root" : ""
# }
# '''
#
# print json_string
#
# json_object = json.loads(json_string)
#
# print 'json_object', json_object
#
# json_object["00_Pipeline"] = "P:/hello/"
#
# new_string = json.dumps(json_object, indent=2)
#
# print 'new_string', new_string
#
# with open("PZ_Config.json", "w") as f:
#     f.write(new_string)

with open("PZ_Config.json") as f:
    data = json.load(f)  # load json data into python object

data["00_Pipeline"] = ""  # change python data

with open('PZ_Config.json', 'w') as f:
    json.dump(data, f, indent=2)  # dump python data into a new json
