# 2. Add Two Numbers

link: [https://leetcode.com/problems/add-two-numbers/](https://leetcode.com/problems/add-two-numbers/)

## Difficulty
Medium

## 题目

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```


Accepted
1,421,674

Submissions
4,227,757

## 问题描述
两个链表形式的整数求和

## 题目分析
注意进位以及链表的生成即可

## 代码实现

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        to_add = 0
        result = ListNode(0)
        p = result
        while l1 or l2 or to_add != 0:
            if l1 is None:
                l1_val = 0
            else:
                l1_val = l1.val
            if l2 is None:
                l2_val = 0
            else:
                l2_val = l2.val
            this_data = l1_val + l2_val + to_add
            to_add = this_data // 10
            this_data = this_data % 10
            p.next = ListNode(this_data)
            p = p.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            
        return result.next
```

## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 88 ms	| 13.8 MB	| python3|

Runtime: 88 ms, faster than 26.68% of Python3 online submissions for Add Two Numbers.

Memory Usage: 13.8 MB, less than 74.99% of Python3 online submissions for Add Two Numbers.