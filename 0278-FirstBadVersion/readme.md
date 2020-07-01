# 70. Climbing Stairs

link: [https://leetcode.com/problems/first-bad-version/](https://leetcode.com/problems/first-bad-version/)

## Difficulty
Easy

## 题目

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:
```
Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 
```

Accepted
422,578
Submissions
1,197,497

## 问题描述
通过给定函数isBadVersion(version)，找出最早出错的版本号

## 题目分析
简单的二分查找应用，注意当第mid结果为true时，此时取值范围是[0, mid]，当结果false时，取值范围是[mid + 1, n]

## 代码实现

```python
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n
        while low < high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return low
        
```

## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 		28 ms	| 13.7 MB		| python3|

Runtime: 28 ms, faster than 74.41% of Python3 online submissions for First Bad Version.
Memory Usage: 13.7 MB, less than 92.06% of Python3 online submissions for First Bad Version.