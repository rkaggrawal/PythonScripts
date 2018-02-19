#!/usr/bin/pyhton

# DEBUG: 10
# INFO: 20
# WARNING: 30
# ERROR: 40
# CRITICAL: 50

import logging
import employee1
logging.basicConfig(filename='/logs/sample1.log', level=logging.DEBUG,
                    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s' )


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

num_1 = 10
num_2 = 5

add_result = add(num_1, num_2)
sub_result = subtract(num_1, num_2)
mul_result = multiply(num_1, num_2)
divide_result = divide(num_1, num_2)

# print ("Add: {} + {} = {}".format(num_1, num_2, add_result))
# print ("Sub: {} - {} = {}".format(num_1, num_2, sub_result))
# print ("Mul: {} * {} = {}".format(num_1, num_2, mul_result))
# print ("Div: {} * {} = {}".format(num_1, num_2, divide_result))

# logging.debug("Add: {} + {} = {}".format(num_1, num_2, add_result))
# logging.debug(("Sub: {} - {} = {}").format(num_1, num_2, sub_result))
# logging.debug("Mul: {} * {} = {}".format(num_1, num_2, mul_result))
# logging.debug("Div: {} * {} = {}".format(num_1, num_2, divide_result))
#
logging.warning("Add: {} + {} = {}".format(num_1, num_2, add_result))
logging.warning(("Sub: {} - {} = {}").format(num_1, num_2, sub_result))
logging.warning("Mul: {} * {} = {}".format(num_1, num_2, mul_result))
logging.warning("Div: {} * {} = {}".format(num_1, num_2, divide_result))
