from typing import Optional


class TrieNode:

    def __init__(self):
        self.name = False
        self.children = [None] * 10
        self.is_leaf = None


class FastPhone:

    def __init__(self):
        self.cur_number = ""
        self.root = TrieNode()
        self.find_num = self.root

    def add_number(self, number: str, person: str):

        # If length of number string is less than 3 or more than 10, we raise a Value Error
        if len(number) < 3 or len(number) > 10:
            raise ValueError("Number can't be added for " + person)

        node = self.root

        for i in range(len(number)):
            # Check if the number already exists in the tree
            if not node.children[int(number[i])]:
                node.children[int(number[i])] = TrieNode()

            # is_leaf represents if the number has already been processed completely and is at the leaf of the tree
            node.is_leaf = False
            node = node.children[int(number[i])]

            # Check prefix of current number exists already saved
            if i < len(number) - 1 and node.is_leaf:
                raise ValueError("Number can't be added for " + person)

        # Check if the current number is a prefix of existing number
        if node.is_leaf is not None and not node.is_leaf:
            raise ValueError("Number can't be added for " + person)

        node.is_leaf = True

        # save the name when the number is saved successfully
        node.name = person

    # Get all possible content for the current prefix
    def get_children(self, node):
        if not node:
            return []
        if node.is_leaf:
            return [node.name]
        values = []
        for i in range(10):
            values += self.get_children(node.children[i])
        return values

    def dial(self, digit: str) -> Optional[str]:

        # We go over the digits and traverse through our Trie to see if there's a match for a user or not
        digit = int(digit)
        self.find_num = self.find_num.children[digit]
        values = self.get_children(self.find_num)

        # When we get a match, we send the first one out and set our find_num node to root again, else KeyError
        if len(values) == 1:
            self.find_num = self.root
            return values[0]
        elif len(values) == 0:
            raise KeyError
        return None
