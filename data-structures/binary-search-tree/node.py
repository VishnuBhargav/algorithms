#!/bin/python


class node:
    def __init__(self, value):
        self.parent = None
        self.left = None
        self.right = None
        self.value = value


def nodeTest():
    node1 = node(1)
    print(node1.value)


if (__name__ == '__main__'):
    nodeTest()
