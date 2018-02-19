#!/usr/bin/python

import keystoneclient.v2_0.client as ksclient
import glanceclient.v2.client as glclient

# Replace the values below  the ones from your local config,
aurl = "http://10.209.245.66:5000/v2.0"
user = "admin"
pwd = "vrp@123"
tname = "admin"
rgname="RegionOne"
#keystone = ksclient.Client(auth_url=aurl, username=user,password=pwd, tenant_name=tname,region_name=rgname)
keystone = ksclient.Client(auth_url=aurl, username=user,password=pwd)
print "Token id is: ",keystone.auth_token
print "Tenant id is: ",keystone.tenants.list()

'''
#glance_endpoint = "http://10.209.245.66:9292"
glance_endpoint = keystone.service_catalog.url_for(service_type='image')
print "glance_endpoint: ",glance_endpoint
glance = glclient.Client(glance_endpoint, token=keystone.auth_token)
images = glance.images.list()
 
for image in images:
    print image['name'], "\t\t",  image['id'], "\t\t", image['min_disk']

'''

#username='admin'
#password='admin'
#tenant_name='admin'
#auth_url='http://10.209.245.66:5000/v2.0'
#auth = v2.Password(username=username, password=password,tenant_name=tenant_name, auth_url=auth_url)
#sess = session.Session(auth=auth)
#keystone = client.Client(session=sess)
