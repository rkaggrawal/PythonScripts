#!/usr/bin/python

import collections 
import simplejson as json
import sys
import os 
import commands
import re
import SSHLibrary
#import vrts_logger


def get_openstack_token_id(openstack_host, user_name, password, tenant):
    """
    Description: This function is used to get the token-id from the openstack
    It takes 4 arguments : openstack hostname or ip, openstack user_name, openstack password and tenant
    
    Author:  Rahul K Aggrawal
    """
    
    #vrts_logger.info(" :: Entering ")
    authDict = {}
    pwdCredDict = {}
    jsonFname = "authJSON.txt"
    tokenOutFname = "tokenOut.txt"
    tokenErrFname = "tokenErr.txt"
    if os.path.exists(jsonFname):
        os.remove(jsonFname)
        #vrts_logger.info(" Successfully removed the existing %s file " % jsonFname)
        print(" Successfully removed the existing %s file " % jsonFname)
    authDict['tenantName'] = tenant
    pwdCredDict['username'] = user_name
    pwdCredDict['password'] = password
    authDict['passwordCredentials'] = pwdCredDict
    finalJSON = {"auth":authDict}    
    with open(jsonFname, 'a') as outfile:
        json.dump(finalJSON, outfile)
    getTokenCmd = "curl http://" + openstack_host + ":5000/v2.0/tokens -d @" +  jsonFname + " -H \"Content-Type: application/json\" > "  +  tokenOutFname + " 2> " + tokenErrFname'//'
    #vrts_logger.info(" Executing Command :: " + getTokenCmd)
    print(" Executing Command :: " + getTokenCmd)
    returnValue = os.system(getTokenCmd)
    if (returnValue != 0):
        errFileHandler = open(tokenErrFname, "r")
        errorMsg = errFileHandler.read()
        errFileHandler.close()
        raise Exception(" Method workflow_verification::get_openstack_token_id : Execution of getTokenCmd Failed . Error Message :: " + errorMsg)
    jsonFileHandler = open(tokenOutFname, "r")
    jsonInfo = jsonFileHandler.read()
    jsonFileHandler.close()
    #print "Json info is: \n",jsonInfo
    jsonInfo =  json.loads(jsonInfo)
    #print "Json info is: \n",jsonInfo
    #validate_tokenOutput(jsonInfo)
    token_id = jsonInfo["access"]["token"]["id"]
    tenant_id = jsonInfo["access"]['token']['tenant']['id']
    #vrts_logger.info( " token_id::" + str(token_id) + " and " + " tenant_id::" + str(tenant_id))
    #vrts_logger.info(" :: Exiting ")
    #print "Token id is: ",token_id
    #print "Tenant id is: ",tenant_id
    return (token_id, tenant_id) 
#list=get_openstack_token_id('10.209.245.66','user_rahul','rahul','project_rahul')
list=get_openstack_token_id('10.209.245.66','admin','vrp@123','admin')

print "Token id is: ",list[0]
print "Tenant id is: ",list[1]


def get_openstack_image_details(token_id, tenant_id, openstack_host):
    """
    Description: This function is used to get the volume details from openstack
    It takes 3 arguments : openstack token_id, openstack tenant_id and openstack hostname or ip
    
    Author:  Rahul K Aggrawal
    """
    
    #vrts_logger.info(" :: Entering ")
    getImageOutFname = "imageOut.txt"
    imageErrFname = "imageErr.txt"
    getImageDetailsCmd = "curl -X GET -s -H \"X-Auth-Token:" + token_id + "\"" + " -H \"Content-Type: application/json\"" + " http://" + openstack_host + ":9292/v1/ >" +  getImageOutFname + " 2> " + imageErrFname
    #vrts_logger.debug(" Executing Command :: " + getImageDetailsCmd)
    print(" Executing Command :: " + getImageDetailsCmd)
    returnValue = os.system(getImageDetailsCmd)
    if (returnValue != 0):
        errFileHandler = open(imageErrFname, "r")
        errorMsg = errFileHandler.read()
	errFileHandler.close()
        raise Exception(
            " Method workflow-verification::get_openstack_image_details : Execution of getImageDetailsCmd Failed.Error Message :: " + errorMsg)
    #validate_apiGetOutput(getImageOutFname, "image")
    jsonFH = open(getImageOutFname, "r")
    imageInfoJSON = jsonFH.read()
    jsonFH.close()
    imageInfoJSON = json.loads(imageInfoJSON)
    image_name = imageInfoJSON["images"]
    #vrts_logger.info(" :: Exiting ")
    return (image_name)

dict = get_openstack_image_details(list[0],list[1],'10.209.245.66')
print "my image is: ",dict[0]["name"]
