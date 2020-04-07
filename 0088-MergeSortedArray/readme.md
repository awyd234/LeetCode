# 88. Merge Sorted Array

link: [https://leetcode.com/problems/merge-sorted-array/](https://leetcode.com/problems/merge-sorted-array/)

## Difficulty
Easy

## 题目

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:
```
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
```
Accepted
516,621
Submissions
1,344,211


## 问题描述
合并有序list的问题，只不过需要把第二个数组合并进第一个数组里

## 题目分析
逆序遍历，这样可以减少元素移动次数


## 代码实现

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num1_index = m - 1
        num2_index = n - 1
        new_num1_index = m + n - 1
        while num1_index >= 0 and num2_index >= 0:
            if nums1[num1_index] > nums2[num2_index]:
                nums1[new_num1_index] = nums1[num1_index]
                num1_index -= 1
            else:
                nums1[new_num1_index] = nums2[num2_index]
                num2_index -= 1
            new_num1_index -= 1
        while num2_index >= 0:
            nums1[num2_index] = nums2[num2_index]
            num2_index -= 1
```



## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 		32 ms	| 14 MB		| python3|

Runtime: 32 ms, faster than 84.56% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 14 MB, less than 6.15% of Python3 online submissions for Merge Sorted Array.
