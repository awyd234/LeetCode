# 387. First Unique Character in a String

link: [https://leetcode.com/problems/first-unique-character-in-a-string/](https://leetcode.com/problems/first-unique-character-in-a-string/)

## Difficulty
Easy

## 题目

Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:
```
s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
```

**Note**: You may assume the string contains only lowercase English letters.

Accepted
532,063
Submissions
999,696

## 问题描述
找出字符串中第一个不重复的字符

## 题目分析
记录每个字符出现的第一次顺序，以及每个字符出现的次数，再次扫描检查第一个出现了1次的字符

## 代码实现

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters_list = []
        letters_dict = {}
        for index, each_str in enumerate(s):
            if each_str not in letters_dict:
                letters_dict[each_str] = 0
                letters_list.append([each_str, index])
            letters_dict[each_str] += 1
        for each_str, index in letters_list:
            if letters_dict.get(each_str) == 1:
                return index
        return -1
```

## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 		124 ms	| 15.1 MB		| python3|

Runtime: 52 ms, faster than 60.56% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.1 MB, less than 43.84% of Python3 online submissions for Move Zeroes.