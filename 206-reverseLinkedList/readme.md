# 206. Reverse Linked List

link: [https://leetcode.com/problems/reverse-linked-list/submissions/](https://leetcode.com/problems/reverse-linked-list/submissions/)

## Difficulty
Easy

## 题目

Reverse a singly linked list.

Example:
```
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

Accepted
875,396
Submissions
1,452,149


## 问题描述
单链表反转问题

## 题目分析
设计好临时节点，不要丢失线索即可，可以手动模拟每一次删除，针对这题可以加一个临时虚拟头结点，避免头部节点丢失


## 代码实现

```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        first_node = ListNode(0)
        first_node.next = head
        tail = head
        while tail.next:
            first_node.next = tail.next
            tail.next = tail.next.next
            first_node.next.next = head
            head = first_node.next
        return first_node.next
```



## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 	28 ms	| 15.4 MB		| python3|

Runtime: 28 ms, faster than 95.05% of Python3 online submissions for Reverse Linked List.
Memory Usage: 15.4 MB, less than 25.00% of Python3 online submissions for Reverse Linked List.
