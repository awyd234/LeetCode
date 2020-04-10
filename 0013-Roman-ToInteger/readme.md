# 13. Roman to Integer

link: [https://leetcode.com/problems/roman-to-integer/](https://leetcode.com/problems/roman-to-integer/)

## Difficulty
Easy

## 题目


Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.
- Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:
```
Input: "III"
Output: 3
```

Example 2:
```
Input: "IV"
Output: 4
```

Example 3:
```
Input: "IX"
Output: 9
```

Example 4:
```
Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
```

Example 5:
```
Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

Accepted
626,031
Submissions
1,141,605

## 问题描述
给定一个banned的list，遍历字符串中，找到最常出现的单词，忽略大小写

## 题目分析
没啥好说的，只不过不用排序，只取最大一个，那拿一个变量保存即可


## 代码实现

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_value_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        this_stack = []
        result = 0
        for each_str in s:
            if len(this_stack) == 0:
                this_stack.append(each_str)
            elif isinstance(this_stack[-1], int):
                if symbol_value_dict[each_str] > this_stack[-1]:
                    this_stack.append(symbol_value_dict[each_str] - this_stack.pop())
                else:
                    result += this_stack.pop()
                    this_stack.append(each_str)
            elif symbol_value_dict[this_stack[-1]] > symbol_value_dict[each_str]:
                result += symbol_value_dict[this_stack.pop()]
                this_stack.append(each_str)
            elif symbol_value_dict[this_stack[-1]] < symbol_value_dict[each_str]:
                top_data = symbol_value_dict[this_stack.pop()]
                now_data = symbol_value_dict[each_str]
                data = now_data - top_data
                this_stack.append(data)
            else:
                this_stack.append(each_str)
            # print(result, this_stack, each_str)
        # print(this_stack)
        for each_data in this_stack:
            if isinstance(each_data, int):
                result += each_data
            else:
                result += symbol_value_dict[each_data]
        return result
```



## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 		40 ms	| 13.8 MB		| python3|

Runtime: 40 ms, faster than 88.81% of Python3 online submissions for Roman to Integer.
Memory Usage: 13.8 MB, less than 5.38% of Python3 online submissions for Roman to Integer.