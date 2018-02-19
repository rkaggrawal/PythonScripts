#!/usr/bin/pyhton

# DEBUG: 10
# INFO: 20
# WARNING: 30
# ERROR: 40
# CRITICAL: 50


import logging
import employee2
#logging.basicConfig(filename='logs/sample2.log', level=logging.DEBUG, \
                    # format='%(asctime)s | %(name)s | %(levelname)s | %(message)s' )

# logger = logging.getLogger(__name__)
logger = logging.getLogger('some')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')

file_handler = logging.FileHandler('logs/sample2.log')
file_handler.setFormatter(formatter)
# file_handler.setLevel(logging.ERROR)
logger.addHandler(file_handler)
file_handler.setLevel(40)


stream_hadler = logging.StreamHandler()
stream_hadler.setLevel(logging.DEBUG)
stream_hadler.setFormatter(formatter)
logger.addHandler(stream_hadler)

file_handler2 = logging.FileHandler('logs/sample_debug.log')
file_handler2.setFormatter(formatter)
file_handler2.setLevel(logging.CRITICAL)
logger.addHandler(file_handler2)




def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

# def divide(x, y):
#     return x / y

def divide(x, y):
    try:
        result =  x / y
    except ZeroDivisionError as Err:
        #logger.exception('Error is: {}'.format(Err))
        logger.error('Error is: {}'.format(Err))

    else:
        return result

num_1 = 10
num_2 = 5

add_result = add(num_1, num_2)
# print ("Add: {} + {} = {}".format(num_1, num_2, add_result))
logger.debug("Add: {} + {} = {}".format(num_1, num_2, add_result))
# logging.debug("Add: {} + {} = {}".format(num_1, num_2, add_result))
# logging.warning("Add: {} + {} = {}".format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
# print ("Sub: {} - {} = {}".format(num_1, num_2, sub_result))
logger.debug(("Sub: {} - {} = {}").format(num_1, num_2, sub_result))
#logging.debug(("Sub: {} - {} = {}").format(num_1, num_2, sub_result))
# logging.warning(("Sub: {} - {} = {}").format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
# print ("Mul: {} * {} = {}".format(num_1, num_2, mul_result))
logger.debug("Mul: {} * {} = {}".format(num_1, num_2, mul_result))
# logging.debug("Mul: {} * {} = {}".format(num_1, num_2, mul_result))
# logging.warning("Mul: {} * {} = {}".format(num_1, num_2, mul_result))

divide_result = divide(num_1, num_2)
# print ("Div: {} * {} = {}".format(num_1, num_2, divide_result))
logger.critical("Div: {} / {} = {}".format(num_1, num_2, divide_result))
# logging.debug("Div: {} / {} = {}".format(num_1, num_2, divide_result))
# logging.warning("Div: {} / {} = {}".format(num_1, num_2, divide_result))
