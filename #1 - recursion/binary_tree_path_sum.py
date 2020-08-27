"""
Given a binary tree and a number ‘S’,
find if the tree has a path from root-to-leaf
such that the sum of all the node values of that path equals ‘S’.
"""


class Node:
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left


def has_path(node, target_sum):
    # If node doesn't exist, then we haven't found the sum - base case for returning False
    if not node:
        return False

    # If the node value equals the target sum and there are no more nodes,
    # then we have found the path -> since it's root to leaf
    # This is a base case as well for returning True
    if node.val == target_sum and not node.left and not node.right:
        return True

    # We check if the path exists by removing the value of the current node,
    # and checking if the left/right node can fulfill the condition
    # This is a cursive case where we do the recursion
    return has_path(node.right, target_sum - node.val) \
           or has_path(node.left, target_sum - node.val)


def setup():
    node = Node(7)
    node.right = Node(9)
    node.left = Node(5)
    node.left.left = Node(2)
    node.left.right = Node(6)
    node.right.left = Node(8)
    node.right.right = Node(10)

    print(has_path(node, 14))


if __name__ == '__main__':
    setup()
