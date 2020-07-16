from utils import TreeNode


class Solution:
    def rightSideView(self, root: TreeNode):
        result = []
        queue = []
        if root is None:
            return []
        queue.append([root, 0])
        last_depth = 0
        last_value = None
        while queue:
            node, depth = queue[0]
            queue.pop(0)
            if depth != last_depth:
                last_depth = depth
                if last_value is not None:
                    result.append(last_value)
            last_value = node.val
            if node.left:
                queue.append([node.left, depth + 1])
            if node.right:
                queue.append([node.right, depth + 1])
        result.append(last_value)
        return result


if __name__ == '__main__':
    solution = Solution()
    this_input = list()
    this_input.append([[1, 2, 3, None, 5, None, 4], [1, 3, 4]])
    this_input.append([[1, 2], [1, 2]])
    this_input.append([[], []])
    for each_value in this_input:
        tree_root = TreeNode.build_normal_tree_by_node_list(each_value[0])
        assert solution.rightSideView(tree_root) == each_value[1]
