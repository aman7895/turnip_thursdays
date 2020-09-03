# week_2

### breadth-first-search

This week I focused on using BFS with queue (instead of my go-to recursion methods).

The idea is simple here. We traverse through the breadth of a tree/graph instead of it's depth (DFS).
Queue is suitable here because we can pop the first element and then traverse through the nodes of the popped element.

We use `deque` from the `collections` package in Python to implement the queue.

While I solved a bunch of questions on this, I have given a very basic [example](/%232%20-%20bfs/binary_tree_level_order_reversal.py) for this topic.
The idea can be used for multiple questions related to tree traversal (zig-zag traversal, reverse level, finding depth of tree).

Reference: [Grokking the coding interview - Design Patterns](https://www.educative.io/courses/grokking-the-coding-interview) 