# 242. Valid Anagram

link: [https://leetcode.com/problems/valid-anagram/](https://leetcode.com/problems/valid-anagram/)

## Difficulty
Easy

## 题目

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
```
Input: s = "anagram", t = "nagaram"
Output: true
```

Example 2:
```
Input: s = "rat", t = "car"
Output: false
```

**Note**:
You may assume the string contains only lowercase alphabets.

**Follow up**:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

Accepted
565,155
Submissions
1,000,907

## 问题描述
判断两个字符串是否是Anagram（变位词）

## 题目分析
Anagram的特点是组成字符串用的字母完全相同，统计对比两个字符串各自各个字母出现的次数即可

## 代码实现

```python
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
```

## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 		32 ms	| 14.2 MB		| python3|

Runtime: 32 ms, faster than 97.73% of Python3 online submissions for Valid Anagram.

Memory Usage: 14.2 MB, less than 42.65% of Python3 online submissions for Valid Anagram.