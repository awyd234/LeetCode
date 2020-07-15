# 1490. Clone N-ary Tree

link: [https://leetcode.com/problems/clone-n-ary-tree/](https://leetcode.com/problems/clone-n-ary-tree/)

## Difficulty
Medium

## 题目

Given a root of an N-ary tree, return a deep copy (clone) of the tree.

Each node in the n-ary tree contains a val (int) and a list (List[Node]) of its children.

```java
class Node {
    public int val;
    public List<Node> children;
}
```

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Follow up: Can your solution work for the graph problem?


Example 1:
![example1](narytreeexample1.png)
```
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,null,3,2,4,null,5,6]
```

Example 2:
![example2](narytreeexample2.png)
```
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
```

Constraints:
- The depth of the n-ary tree is less than or equal to 1000.
- The total number of nodes is between [0, 10^4].

Accepted
1,889

Submissions
2,198

## 问题描述
深度copy一棵多叉树

## 题目分析
递归调用函数即可，可以验证，确实是深拷贝，而不是简单的对原树节点的引用

## 代码实现

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""
class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        new_tree = Node(val=root.val)
        for each_child in root.children:
            new_tree.children.append(self.cloneTree(each_child))
        return new_tree
```

## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 		64 ms	| 17.5 MB		| python3|


Runtime: 64 ms, faster than 99.07% of Python3 online submissions for Clone N-ary Tree.

Memory Usage: 17.5 MB, less than 100.00% of Python3 online submissions for Clone N-ary Tree.