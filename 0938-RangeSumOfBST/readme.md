# 938. Range Sum of BST

link: [https://leetcode.com/problems/range-sum-of-bst/](https://leetcode.com/problems/range-sum-of-bst/)

## Difficulty
Easy

## 题目

Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.


Example 1:
```
Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
```

Example 2:
```
Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
```

Note:
- The number of nodes in the tree is at most 10000.
- The final answer is guaranteed to be less than 2^31.

Accepted
214,773

Submissions
265,179

## 问题描述
求BST中在区间[L, R]之前所有节点的和

## 题目分析
根据BST特点判断，去对比左右子树的值即可，或者也可以试试先遍历后求值，不过那样效率肯定会变低

## 代码实现

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
```

## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 276 ms	| 21.7 MB	| python3|

Runtime: 276 ms, faster than 53.36% of Python3 online submissions for Range Sum of BST.

Memory Usage: 21.7 MB, less than 95.49% of Python3 online submissions for Range Sum of BST.