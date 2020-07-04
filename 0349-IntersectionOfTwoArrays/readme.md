# 349. Intersection of Two Arrays

link: [https://leetcode.com/problems/intersection-of-two-arrays/](https://leetcode.com/problems/intersection-of-two-arrays/)

## Difficulty
Easy

## 题目

Given two arrays, write a function to compute their intersection.

Example 1:
```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
```

Example 2:
```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
```

Note:
- Each element in the result must be unique.
- The result can be in any order.

Accepted
361,520

Submissions
584,086

## 问题描述
求两个数组的去重后的交集

## 题目分析
既然没有顺序要求，直接用set类型中的内嵌方法即可

## 代码实现

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # result_list = []
        # result_set = set()
        # nums1_set = set(nums1)
        # nums2_set = set(nums2)
        # for each_data in nums1_set:
        #     if each_data in nums2_set and each_data not in result_set:
        #         result_list.append(each_data)
        #         result_set.add(each_data)
        # return result_list
        return list(set(nums1).intersection(set(nums2)))
```

## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 		48 ms	| 13.9 MB		| python3|

Runtime: 48 ms, faster than 60.70% of Python3 online submissions for Intersection of Two Arrays.

Memory Usage: 13.9 MB, less than 55.56% of Python3 online submissions for Intersection of Two Arrays.