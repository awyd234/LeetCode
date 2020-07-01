# 14. Longest Common Prefix

link: [https://leetcode.com/problems/longest-common-prefix/](https://leetcode.com/problems/longest-common-prefix/)

## Difficulty
Easy

## 题目

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
```
Input: ["flower","flow","flight"]
Output: "fl"
```

Example 2:
```
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

Note:
All given inputs are in lowercase letters a-z.

Accepted
748,643
Submissions
2,124,054

## 问题描述
找出所有字符串中的最长前缀

## 题目分析
太简单了，没啥好说的，注意好边界条件即可，但是如果是找出n个字符串中的公共子字符串，这个问题可以研究下

## 代码实现

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        max_length = min([len(_) for _ in strs]) if len(strs) != 0 else 0
        for index in range(max_length):
            if all([_[index] == strs[0][index] for _ in strs[1:]]):
                result += strs[0][index]
            else:
                break
        return result
```

## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 		28 ms	| 14 MB		| python3|

Runtime: 28 ms, faster than 92.50% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 14 MB, less than 45.67% of Python3 online submissions for Longest Common Prefix.