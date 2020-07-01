# 283. Move Zeroes

link: [https://leetcode.com/problems/move-zeroes/](https://leetcode.com/problems/move-zeroes/)

## Difficulty
Easy

## 题目

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
```
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
```

Note:
- You must do this in-place without making a copy of the array.
- Minimize the total number of operations.

Accepted
831,511
Submissions
1,443,780

## 问题描述
将所有0移动到最末尾去，同时保证其他数据的顺序

## 题目分析
记录有多少个0，采用删除array元素的常规移动方法，最后按0的个数追加替换上去

## 代码实现

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        for index, each_data in enumerate(nums):
            if each_data == 0:
                zero_count += 1
                continue
            nums[index - zero_count] = each_data
        start = index - zero_count + 1
        while start < len(nums):
            nums[start] = 0
            start += 1

```

## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 		52 ms	| 15.1 MB		| python3|

Runtime: 52 ms, faster than 60.56% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.1 MB, less than 43.84% of Python3 online submissions for Move Zeroes.