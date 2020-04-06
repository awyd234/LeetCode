# 415. Add Strings

link: [https://leetcode.com/problems/add-strings/](https://leetcode.com/problems/add-strings/)

## Difficulty
Easy

## 题目

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

- The length of both num1 and num2 is < 5100.
- Both num1 and num2 contains only digits 0-9.
- Both num1 and num2 does not contain any leading zero.
- You must not use any built-in BigInteger library or convert the inputs to integer directly.

Accepted
155,253
Submissions
335,019

## 问题描述
大数计算问题

## 题目分析
注意进位和边界条件即可


## 代码实现

```python
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        num1_list = list(num1)
        num2_list = list(num2)
        the_next = 0
        for each_index in range(1, len(num1_list) + 1):
            number1 = num1_list[-each_index]
            if each_index > len(num2_list):
                number2 = '0'
            else:
                number2 = num2_list[-each_index]
            this_num = ord(number1) + ord(number2) - 2 * ord('0') + the_next
            num1_list[-each_index] = chr(this_num % 10 + ord('0'))
            the_next = this_num // 10
        output = ''.join(num1_list)
        if the_next != 0:
            output = chr(the_next + ord('0')) + output
        return output
```



## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 	36 ms	| 14 MB		| python3|

Runtime: 36 ms, faster than 81.26% of Python3 online submissions for Add Strings.
Memory Usage: 14 MB, less than 5.55% of Python3 online submissions for Add Strings.