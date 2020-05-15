#!/usr/bin/python


class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

            else:
                print "Value already exists"

        else:
            self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print self.data
        if self.right:
            self.right.print_tree()

    def children_count(self):
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt



print("Data in Binary Search Tree:")
bst = Node()
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(4)
bst.insert(14)
bst.insert(13)
bst.print_tree()
