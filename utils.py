# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_bst_method1(data: list):
    if len(data) == 0 or all([_ is None for _ in data]):
        return None
    root_node = TreeNode(val=data[0])
    for each_data in data[1:]:
        if each_data is None:
            continue
        this_node = TreeNode(val=each_data)
        p = root_node
        while p:
            if this_node.val < p.val:
                if p.left:
                    p = p.left
                else:
                    p.left = this_node
                    break
            elif this_node.val > p.val:
                if p.right:
                    p = p.right
                else:
                    p.right = this_node
                    break
    return root_node
