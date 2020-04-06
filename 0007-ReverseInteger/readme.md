#7. Reverse Integer

link: [https://leetcode.com/problems/reverse-integer/](https://leetcode.com/problems/reverse-integer/)

## Difficulty
Easy

## 题目

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
```
Input: 123
Output: 321
```
Example 2:
```
Input: -123
Output: -321
```
Example 3:
```
Input: 120
Output: 21
```
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Accepted
1,005,951
Submissions
3,924,468

## 问题描述
整数翻转，如果结果超出了范围，需要返回0

## 题目分析
将每一个位提取为一个个的数字，然后再相乘即可，这里直接用2 ** 31取巧了，也可以将数字转为2进制再对比


## 代码实现

```python
class Solution:
    def reverse(self, x: int) -> int:
        x_list = []
        negtive = 1
        if x < 0:
            negtive = -1
            x = -x
        while x > 0:
            x_list.append(x % 10)
            x //= 10
        output = 0
        coefficient = 1
        for each_index, each_num in enumerate(x_list[::-1]):
            output += each_num * coefficient
            coefficient *= 10
        output *= negtive
        if output >= 2 ** 31 or output < -2 ** 31:
            output = 0
        return output
            
```



## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 	28 ms	| 14 MB		| python3|

Runtime: 28 ms, faster than 78.06% of Python3 online submissions for Reverse Integer.
Memory Usage: 14 MB, less than 5.26% of Python3 online submissions for Reverse Integer.