#!/usr/bin/python

import boto3
s3 = boto3.resource('s3')

#for bucket in s3.buckets.all():
    #print(bucket.name)

data = open('/home/raggrawa/python_scripts/bin/add_host_svm11_svm28.txt', 'rb')
s3.Bucket('rka-test-pune').put_object(Key='add_host_svm11_svm28.txt', Body=data)

#s3.create_bucket(Bucket='rka-test-pune2')
