#!/bin/python
from node import node


class bst:

    def __init__(self):
        self.root = None

    def insert(self, t):
        if(self.root is None):
            self.root = t
        else:
            node = self.root
            while(True):
                if(node.value <= t.value):
                    if(node.right is None):
                        node.right = t
                        t.parent = node
                        break
                    else:
                        node = node.right
                elif(node.value > t.value):
                    if(node.left is None):
                        node.left = t
                        t.parent = node
                        break
                    else:
                        node = node.left
        return t

    def traverseNode(self, node):
        if(node is not None):
            if(node.left is not None):
                self.traverseNode(node.left)
            print(node.value)
            if(node.right is not None):
                self.traverseNode(node.right)

    def inOrderTraversal(self):
        node = self.root
        self.traverseNode(node)


def testBst():
    bstTest = bst()
    bstTest.insert(node(235))
    bstTest.insert(node(2214))
    bstTest.insert(node(21241))
    bstTest.insert(node(5123))
    bstTest.insert(node(242))
    bstTest.insert(node(211))
    bstTest.insert(node(5))
    bstTest.insert(node(242))
    bstTest.insert(node(2142))
    bstTest.insert(node(255))
    bstTest.insert(node(27768))
    bstTest.insert(node(8521))
    bstTest.insert(node(58463))
    bstTest.insert(node(2357))
    bstTest.insert(node(2147))
    bstTest.inOrderTraversal()


if(__name__ == '__main__'):
    testBst()
