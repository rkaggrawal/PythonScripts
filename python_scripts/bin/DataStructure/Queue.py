#!/usr/bin/python

from collections import deque

class Queue():
    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        self.queue.append(data)
        #print self.queue

    def dequeue(self):
        if len(self.queue) == 0:
            raise Exception("Queue is empty")
        return self.queue.popleft()

    def search(self, data):
        if data in self.queue:
            return True
        else:
            return False

    def size(self):
        return len(self.queue)

    def displayQueue(self):
        print self.queue
        # for item in self.items:
        #     print item



q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.displayQueue()
print 'Size of q is %d' % q.size()

q.dequeue()
q.dequeue()
q.displayQueue()
print 'Size of q is %d' % q.size()

