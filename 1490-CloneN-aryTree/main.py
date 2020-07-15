# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def cloneTree(self, root: Node) -> Node:
        if root is None:
            return None
        new_tree = Node(val=root.val)
        for each_child in root.children:
            new_tree.children.append(self.cloneTree(each_child))
        return new_tree

