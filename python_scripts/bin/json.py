#!/usr/bin/python
#import demjson
#import simplejson as json

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

json = json.dump(data)
print json

json = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

text = demjson.decode(json)
print  text

authDict = {}
pwdCredDict = {}
jsonFname = "authJSON.txt"
authDict['tenantName'] = "Panorama"
pwdCredDict['username'] = "rohit"
pwdCredDict['password'] = "vrp@123"
authDict['passwordCredentials'] = pwdCredDict
finalJSON = {"auth":authDict}
with open(jsonFname, 'a') as outfile:
       json.dumps(finalJSON, outfile)


json = demjson.encode(finalJSON)
print json

