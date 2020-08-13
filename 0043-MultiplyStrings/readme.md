# 43. Multiply Strings

link: [https://leetcode.com/problems/multiply-strings/](https://leetcode.com/problems/multiply-strings/)

## Difficulty
Medium

## 题目

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:
```
Input: num1 = "2", num2 = "3"
Output: "6"
```

Example 2:
```
Input: num1 = "123", num2 = "456"
Output: "56088"
```

Note:
- The length of both num1 and num2 is < 110.
- Both num1 and num2 contain only digits 0-9.
- Both num1 and num2 do not contain any leading zero, except the number 0 itself.
- You must not use any built-in BigInteger library or convert the inputs to integer directly.


## 问题描述
大数乘法问题

## 题目分析
注意乘法的模拟实现方式，乘数乘以被乘数的每一位然后移位相加

## 代码实现

```python
class Solution:
    def char_to_num(self, char_val):
        return ord(char_val) - ord('0')

    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        all_result = []
        for index, each_str in enumerate(num2[::-1]):
            next_val = 0
            result = ""
            each_num = self.char_to_num(each_str)
            for num1_str in num1[::-1]:
                this_result = self.char_to_num(num1_str) * each_num + next_val
                next_val = this_result // 10
                this_result %= 10
                result = str(this_result) + result
            if next_val != 0:
                result = str(next_val) + result
            for i in range(index):
                result += '0'
            all_result.append(result)
        return_result = ""
        next_val = 0
        index = 0
        while next_val != 0 or any([index < len(each_data)for each_data in all_result]):
            this_data = 0
            for each_data in all_result:
                if index < len(each_data):
                    this_data += self.char_to_num(each_data[-index - 1])
            this_data += next_val
            next_val = this_data // 10
            this_data %= 10
            return_result = str(this_data) + return_result
            index += 1
        index = 0
        while index < len(return_result) and return_result[index] == "0":
            index += 1
        if index == len(return_result):
            return_result = "0"
        else:
            return_result = return_result[index:]
        return return_result
```

Accepted
92,534

Submissions 
210,476


## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 	252 ms	| 13.7 MB		| python3|

Runtime: 252 ms, faster than 25.19% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 13.7 MB, less than 24.78% of Python3 online submissions for Longest Common Prefix.