# 344. Reverse String

link: [https://leetcode.com/problems/reverse-string/](https://leetcode.com/problems/reverse-string/)

## Difficulty
Easy

## 题目

Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.


Example 1:
```
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

Example 2:
```
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

Accepted
760,877

Submissions
1,116,436

## 问题描述
字符串翻转

## 题目分析
很简单的题目，速度为什么这么慢难以理解

## 代码实现

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s_len = len(s)
        for index in range(s_len // 2):
            s[index], s[s_len - index - 1] = s[s_len - index - 1], s[index]
        
```

## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 256 ms	| 18.4 MB	| python3|

Runtime: 256 ms, faster than 15.89% of Python3 online submissions for Reverse String.

Memory Usage: 18.4 MB, less than 18.79% of Python3 online submissions for Reverse String.