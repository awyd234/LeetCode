# 70. Climbing Stairs

link: [https://leetcode.com/problems/climbing-stairs/](https://leetcode.com/problems/climbing-stairs/)

## Difficulty
Easy

## 题目

Count the number of prime numbers less than a non-negative number, n.

Example:
```
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
```

Accepted
355,530
Submissions
1,136,435

## 问题描述
判断比n小的质数有多少个

## 题目分析
可以通过埃拉托色尼筛选法（the Sieve of Eratosthenes）来解决，即从i(i < n)开始，不大于n的i * m都是质数，但是从时间来看还是很长，可能需要寻找更优解

## 代码实现

```python
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        if n == 2:
            return 0
        result = [True] * n
        result[1] = False
        result[2] = True
        for each_num in range(2, int(n ** 0.5) + 1):
            this_index = 2
            if not result[each_num]:
                continue
            while this_index * each_num < n:
                result[this_index * each_num] = False
                this_index += 1
        count = 0
        for each_data in range(2, n):
            if result[each_data]:
                count += 1
        return count
            
        
```

## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 		964 ms	| 25.2 MB		| python3|

Runtime: 964 ms, faster than 39.42% of Python3 online submissions for Count Primes.
Memory Usage: 25.2 MB, less than 87.15% of Python3 online submissions for Count Primes.