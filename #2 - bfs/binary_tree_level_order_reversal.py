"""
problem_statement:
Given a binary tree, populate an array to represent its level-by-level traversal.
You should populate the values of all nodes of each level from left to right in separate sub-arrays.
for example:
input -
    1
  /  \
 2    3
output - [[1],[2,3]]
"""

from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(node):
    # We keep a result array to store the level data
    result = []

    # If the node doesn't exist then we return the empty list
    if not node:
        return result

    # We form a queue to store all the nodes
    queue = deque()
    queue.append(node)

    # While the queue has elements, we traverse through it
    while queue:

        len_queue = len(queue)
        current_level = []

        for _ in range(len_queue):
            # We get the first node of the queue and add it to the current level
            # We also extract the right or left nodes of the current node
            current_node = queue.popleft()
            current_level.append(current_node.val)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        # We append all the current nodes to the result and then continue
        result.append(current_level)

    return result


def main():
    root = Node(12)
    root.left = Node(7)
    root.right = Node(1)
    root.left.left = Node(9)
    root.right.left = Node(10)
    root.right.right = Node(5)
    print("Level order traversal: " + str(traverse(root)))


if __name__ == '__main__':
    main()
