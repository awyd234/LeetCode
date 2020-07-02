# 198. House Robber

link: [https://leetcode.com/problems/house-robber/](https://leetcode.com/problems/house-robber/)

## Difficulty
Easy

## 题目

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

 
Example 1:
```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
```

Example 2:
```
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
``` 

Constraints:
- 0 <= nums.length <= 100
- 0 <= nums[i] <= 400

Accepted
514,438
Submissions
1,228,138

## 问题描述
一个数组，不能连续取数，给出取出数字和的最大值

## 题目分析
DP问题，设f(n)为取前n个数字时能得到的最大值，可以写成 f(n) = max(f(n - 2), f(n - 1) + a[n], f(n - 3) + a[n])


## 代码实现

```python
class Solution:
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        elif len(nums) == 3:
            return max([nums[0] + nums[2], nums[1]])
        else:
            rob_nums = [0, nums[0], nums[1], max([nums[0] + nums[2], nums[1]])]
        for each_index, each_data in enumerate(nums):
            if each_index <= 2:
                continue
            rob_nums.append(max([rob_nums[each_index], rob_nums[each_index - 1] + each_data, rob_nums[each_index - 2] + each_data]))
        return rob_nums[-1]

```

## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 		32 ms	| 13.8 MB		| python3|

Runtime: 32 ms, faster than 58.99% of Python3 online submissions for House Robber.

Memory Usage: 13.8 MB, less than 71.48% of Python3 online submissions for House Robber.