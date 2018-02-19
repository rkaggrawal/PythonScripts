class Node:


    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self,data):
        if self.value == data:
            return False

        elif data < self.value:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True

        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(self.value)
            if self.right:
                self.right.inorder()

class BTree:


    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def inorder(self):
            print "Inorder Traversal"
            self.root.inorder()



bst = BTree()
## bst = BTree(8)
bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(4)
bst.insert(14)
bst.insert(13)
bst.inorder()