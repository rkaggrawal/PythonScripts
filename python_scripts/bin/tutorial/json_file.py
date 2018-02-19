#!/usr/bin/python

import json

q = []
q.append({"fname":"aman", "lname":"kapoor"})
q.append({"fname":"raj", "lname":"verma"})
print q

print "\n" + json.dumps(q, indent=4) #Converts regular dict/list format into json format


q.append({"fname":"sachin", "lname":"apte"})
fh = open("json_out", "w")
json.dump(q, fh, indent=4)
fh.close()

fr = open("json_out", "r")
jsondata = fr.read()
fr.close()

print jsondata
print "\n",json.loads(jsondata) #coverts json format into regular dict/list format
