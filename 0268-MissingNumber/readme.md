# 268. Missing Number

link: [https://leetcode.com/problems/missing-number/solution/](https://leetcode.com/problems/missing-number/solution/)

## Difficulty
Easy

## 题目

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:
```
Input: [3,0,1]
Output: 2
```

Example 2:
```
Input: [9,6,4,2,3,5,7,0,1]
Output: 8
```

Note:
- Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

Accepted
452,291

Submissions
880,080

## 问题描述
找出0-n中的缺失值

## 题目分析
既然数字排列的很整齐，直接从0加到n然后减去所有数字即可，可以用高斯公式快速求完整数组的和；另看到一种方法是用XOR来做

\begin{align}
missing &= 4∧(0∧0)∧(1∧1)∧(2∧3)∧(3∧4) \\
&= (4∧4)∧(0∧0)∧(1∧1)∧(3∧3)∧2 \\
&= 0∧0∧0∧0∧2 \\
&= 2
\end{align}

## 代码实现

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        len_nums = len(nums)
        return len_nums * (len_nums + 1) // 2 - sum(nums)
```

## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 164 ms	| 15 MB	| python3|

Runtime: 164 ms, faster than 31.94% of Python3 online submissions for Missing Number.

Memory Usage: 15 MB, less than 69.42% of Python3 online submissions for Missing Number.