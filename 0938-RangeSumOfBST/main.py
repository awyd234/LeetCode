from utils import TreeNode, build_bst_method1


class Solution:

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        left_val = 0
        right_val = 0
        middle_val = 0
        if root is None:
            return 0
        if L <= root.val <= R:
            middle_val = root.val
            left_val = self.rangeSumBST(root.left, L, R)
            right_val = self.rangeSumBST(root.right, L, R)
        elif root.val < L:
            right_val = self.rangeSumBST(root.right, L, R)
        elif root.val > R:
            left_val = self.rangeSumBST(root.left, L, R)
        return left_val + right_val + middle_val


if __name__ == '__main__':
    solution = Solution()
    this_input = list()
    this_input.append([[10, 5, 15, 3, 7, None, 18], 7, 15, 32])
    for each_value in this_input:
        root_node = build_bst_method1(each_value[0])
        assert solution.rangeSumBST(root_node, each_value[1], each_value[2]) == each_value[3]
