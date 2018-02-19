#!/usr/bin/python

class TestWith:
    def __enter__(self):
        print "I am in enter"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print "I am in exit"

import time

with TestWith():
    print "Sleeping for 10 s"
    time.sleep(10)
