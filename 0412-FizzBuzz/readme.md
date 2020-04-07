# 412. Fizz Buzz

link: [https://leetcode.com/problems/fizz-buzz/](https://leetcode.com/problems/fizz-buzz/)

## Difficulty
Easy

## 题目

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:
```
n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
```
Accepted
298,534
Submissions
485,864

## 问题描述
简单的数字输出

## 题目分析
太水了，没啥好说的，编程语言入门题


## 代码实现

```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result_list = []
        for index in range(1, n + 1):
            if index % 15 == 0:
                result_list.append('FizzBuzz')
            elif index % 3 == 0:
                result_list.append('Fizz')
            elif index % 5 == 0:
                result_list.append('Buzz')
            else:
                result_list.append(str(index))
        return result_list
```



## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 		28 ms	| 14.9 MB		| python3|

Runtime: 28 ms, faster than 99.83% of Python3 online submissions for Fizz Buzz.
Memory Usage: 14.9 MB, less than 6.38% of Python3 online submissions for Fizz Buzz.
