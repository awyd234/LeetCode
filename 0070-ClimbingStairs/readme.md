# 70. Climbing Stairs

link: [https://leetcode.com/problems/climbing-stairs/](https://leetcode.com/problems/climbing-stairs/)

## Difficulty
Easy

## 题目

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
```
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

Example 2:
```
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

Constraints:
- 1 <= n <= 45

Accepted
676,286
Submissions
1,437,898

## 问题描述
一共n级台阶，每次最多爬1级或者2级，一共有多少种方案

## 题目分析
类似Fibonacci的问题，简单的DP，把递归改写成迭代即可

## 代码实现

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        result_list = [0] * (n + 1)
        for index in range(1, n + 1):
            if index == 1:
                result_list[index] = 1
            elif index == 2:
                result_list[index] = 2
            else:
                result_list[index] = result_list[index - 1] + result_list[index - 2]
        return result_list[n]
```

## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 		28 ms	| 13.9 MB		| python3|

Runtime: 28 ms, faster than 74.49% of Python3 online submissions for Climbing Stairs.
Memory Usage: 13.9 MB, less than 38.82% of Python3 online submissions for Climbing Stairs.