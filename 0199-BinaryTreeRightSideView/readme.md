# 199. Binary Tree Right Side View

link: [https://leetcode.com/problems/binary-tree-right-side-view/](https://leetcode.com/problems/binary-tree-right-side-view/)

## Difficulty
Medium

## 题目

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:
```
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
```

Accepted
290,866

Submissions
541,492

## 问题描述
输出一棵二叉树每层最右侧节点的value

## 题目分析
层次遍历即可，queue可以改造下，记录每个节点所在的深度，通过深度对比来确定每一层的最后一个节点，此处可以优化，有多种解

## 代码实现

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
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
```

## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 		32 ms	| 14 MB		| python3|


Runtime: 32 ms, faster than 77.59% of Python3 online submissions for Binary Tree Right Side View.

Memory Usage: 14 MB, less than 25.77% of Python3 online submissions for Binary Tree Right Side View.