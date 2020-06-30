#7. Reverse Integer

link: [https://leetcode.com/problems/valid-palindrome-ii/](https://leetcode.com/problems/valid-palindrome-ii/)

## Difficulty
Easy

## 题目

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
```
Input: "aba"
Output: True
```

Example 2:
```
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
```

Note:
- The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

Accepted
165,576
Submissions
454,741

## 问题描述
判断字符串在最多移除一个字符后是否是回文串

## 题目分析
递归分析，同时字符只能移除一次，所以需要标记是否已经移除过了字符


## 代码实现

```python
class Solution:
    flag = True
    
    def validPalindrome(self, s: str) -> bool:
        first_index = 0
        last_index = len(s) - 1
        while first_index < last_index:
            if s[first_index] == s[last_index]:
                first_index += 1
                last_index -= 1
                continue
            if self.flag:
                self.flag = False
                return self.validPalindrome(s[first_index + 1: last_index + 1]) or self.validPalindrome(s[first_index: last_index])
            else:
                return False
        return True
```


## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 	164 ms	| 14.3 MB		| python3|

Runtime: 164 ms, faster than 64.05% of Python3 online submissions for Valid Palindrome II.
Memory Usage: 14.3 MB, less than 50.67% of Python3 online submissions for Valid Palindrome II.