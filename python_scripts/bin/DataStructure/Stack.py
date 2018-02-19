#!/usr/bin/python

class Stack(object):
    def __init__(self):
        self.items =[]

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if len(self.items) == 0:
            raise Exception("Stack is empty")
        return self.items.pop()

    def search(self, data):
        if data in self.items:
            return True
        else:
            return False
    def size(self):
        return len(self.items)

    def displayStack(self):
        for item in self.items:
            print item


stackObj = Stack()
# stackObj.pop()
stackObj.push('one')
stackObj.push('two')
stackObj.push('three')
stackObj.push('four')
stackObj.displayStack()
stackObj.pop()
stackObj.displayStack()

if stackObj.search('two'):
    print "Found"
else:
    print "Not Found"

print 'Length of stack is %d'  %(stackObj.size())