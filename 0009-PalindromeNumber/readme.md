# 9. Palindrome Number

link: [https://leetcode.com/problems/palindrome-number/](https://leetcode.com/problems/palindrome-number/)

## Difficulty
Easy

## 题目

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
```
Input: 121
Output: true
```

Example 2:
```
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

Example 3:
```
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

**Follow up**:

Coud you solve it without converting the integer to a string?

Accepted
929,682
Submissions
1,938,541

## 问题描述
判断数字是不是回文数

## 题目分析
判断数字是不是回文数比判断回文串要简单一些，如果是负数，那肯定不是，这样数字一定是正数，只要将数字反过来对比和原数字是否相等即可

## 代码实现

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        final_result = 0
        origin_result = x
        while x > 0:
            final_result *= 10
            final_result += (x % 10)
            x //= 10
        if final_result == origin_result:
            return True
        return False
```

## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 		64 ms	| 13.7 MB		| python3|

Runtime: 64 ms, faster than 61.12% of Python3 online submissions for Palindrome Number.
Memory Usage: 13.7 MB, less than 87.64% of Python3 online submissions for Palindrome Number.