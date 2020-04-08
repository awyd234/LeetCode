# 125. Valid Palindrome

link: [https://leetcode.com/problems/valid-palindrome/](https://leetcode.com/problems/valid-palindrome/)

## Difficulty
Easy

## 题目

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
```
Input: "A man, a plan, a canal: Panama"
Output: true
```

Example 2:
```
Input: "race a car"
Output: false
```

Accepted
517,414
Submissions
1,495,513

## 问题描述
判断字符串是否是回文串，只考虑字母和数字，忽略大小写

## 题目分析
前后两个索引，对比即可，注意边界条件


## 代码实现

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        head = 0
        tail = len(s) - 1
        while tail >= 0:
            while not (s[head].isdigit() or s[head].isalpha()):
                head += 1
                if head >= tail:
                    return True
            while not (s[tail].isdigit() or s[tail].isalpha()):
                tail -= 1
                if tail <= head:
                    return True
            if s[head].lower() != s[tail].lower():
                return False
            head += 1
            tail -= 1
        return True
```



## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 		56 ms	| 14.1 MB		| python3|

Runtime: 56 ms, faster than 26.22% of Python3 online submissions for Valid Palindrome.
Memory Usage: 14.1 MB, less than 50.00% of Python3 online submissions for Valid Palindrome.