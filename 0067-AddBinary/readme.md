#67. Add Binary

link: [https://leetcode.com/problems/add-binary/](https://leetcode.com/problems/add-binary/)

## Difficulty
Easy

## 题目

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
```
Input: a = "11", b = "1"
Output: "100"
```

Example 2:
```
Input: a = "1010", b = "1011"
Output: "10101"
```

Constraints:
- Each string consists only of '0' or '1' characters.
- 1 <= a.length, b.length <= 10^4
- Each string is either "0" or doesn't contain any leading zero.

Accepted
445,010
Submissions
1,013,345

## 问题描述
字符串形式的二进制数相加

## 题目分析
模拟加法器，注意进位控制，此处为了保持统一，设a和b长度分别为l和m，取n=max(l, m)，最终结果的长度一定小于等于n + 1


## 代码实现

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        index = 1
        to_add = 0
        result = []
        max_index = max([len(a), len(b)]) + 1
        a = '0' * (max_index - len(a)) + a
        b = '0' * (max_index - len(b)) + b
        while index <= max_index:
            int_a = int(a[-index])
            int_b = int(b[-index])
            this_add = int_a + int_b + to_add
            if this_add > 1:
                to_add = 1
                this_add = this_add - 2
            else:
                to_add = 0
            result.append(this_add)
            index += 1
        result.append(to_add)
        result.reverse()
        start_index = 0
        while len(result) > start_index and result[start_index] == 0:
            start_index += 1
        result = ''.join([str(_) for _ in result[start_index:]])
        if result == '':
            result = '0'
        return result
```


## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 	28 ms	| 13.8 MB		| python3|

Runtime: 28 ms, faster than 87.98% of Python3 online submissions for Add Binary.
Memory Usage: 13.8 MB, less than 51.38% of Python3 online submissions for Add Binary.