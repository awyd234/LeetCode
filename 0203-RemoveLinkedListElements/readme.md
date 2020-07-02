# 203. Remove Linked List Elements

link: [https://leetcode.com/problems/remove-linked-list-elements/](https://leetcode.com/problems/remove-linked-list-elements/)

## Difficulty
Easy

## 题目

Remove all elements from a linked list of integers that have value val.

Example:
```
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
```

Accepted
325,408
Submissions
864,845

## 问题描述
单链表list删去指定元素

## 题目分析
基本的单链表删除操作，需要注意的是没有一个head是指向第一个元素的，为了方便删除可以临时构造一个head指向第一个元素，或者先走一遍while循环过滤最开始的指定元素也可以

## 代码实现

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        none_head = ListNode(0, None)
        none_head.next = head
        p = none_head
        while p and p.next:
            while p.next and p.next.val == val:
                p.next = p.next.next
            p = p.next 
        return none_head.next
```

## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 		76 ms	| 17 MB		| python3|

Runtime: 76 ms, faster than 41.83% of Python3 online submissions for Remove Linked List Elements.

Memory Usage: 17 MB, less than 19.71% of Python3 online submissions for Remove Linked List Elements.