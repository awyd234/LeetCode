# 21. Merge Two Sorted Lists

link: [https://leetcode.com/problems/merge-two-sorted-lists/](https://leetcode.com/problems/merge-two-sorted-lists/)

## Difficulty
Easy

## 题目

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:
```
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```

Accepted 889,805, Submissions 1,718,977


## 问题描述
合并两个有序单链表，按从小到大排列

## 题目分析
就是跟踪两个list，比较大小，然后索引后移，不过这题是个给定的数据结构，需要用到单链表，建一个尾节点指向最后即可


## 代码实现

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        output_node = ListNode(0)
        tail = output_node
        while l1 and l2:
            this_node = ListNode(0)
            this_node.next = None
            if l1.val <= l2.val:
                this_node.val = l1.val
                l1 = l1.next
            else:
                this_node.val = l2.val
                l2 = l2.next
            tail.next = this_node
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return output_node.next
```



## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 36 ms	| 13.9 MB	| python3|

Runtime: 36 ms, faster than 62.66% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.9 MB, less than 6.61% of Python3 online submissions for Merge Two Sorted Lists.