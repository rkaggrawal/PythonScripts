#!/usr/bin/python

import os

print "Env is: ",os.environ['DB']
#os.environ.set['DB'] = 'ORA'

# using get will return `None` if a key is not present rather than raise a `KeyError`
print os.environ.get('MY_NAME')

# os.getenv is equivalent, and can also give a default value instead of `None`
print os.getenv('KEY_NAME', 'rajat')
