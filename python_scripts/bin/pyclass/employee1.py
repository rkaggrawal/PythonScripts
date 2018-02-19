#!/usr/bin/python

# DEBUG: 10
# INFO: 20
# WARNING: 30
# ERROR: 40
# CRITICAL: 50

import logging
logging.basicConfig(filename='logs/employee1.log', level=logging.INFO,
                    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s' )


class Employee:
    "A sample class"
    def __init__(self, first, last):
        self.first = first
        self.last = last
        #print ('Employee created: {} - {}'.format(self.fullname, self.email))
        logging.info('Employee created: {} - {}'.format(self.fullname, self.email))
        #logging.debug('I want to debug')
        #logging.warning('Generating warning')

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def email(self):
        return '{}.{}@trade.tt'.format(self.first, self.last)

emp_1 = Employee('Test1', 'User1')
emp_1 = Employee('Test2', 'User2')

