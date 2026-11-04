# Script for copying content of variable to the provided file on the disk.
import json
'''
req_file = "myjson.json"
fo = open(req_file, 'r')
print(fo.read())
'''
my_dict = {'Name':'Narendra', 'skills':['Python', 'shell', 'AWS']}
req_file = "myjson_copy.json"
fo = open(req_file, 'w')
json.dump(my_dict, fo, indent=4)
fo.close()
my_dict2 = '''


'''