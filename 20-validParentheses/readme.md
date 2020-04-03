# LeetCode - 20. Valid Parentheses

link: [https://leetcode.com/problems/valid-parentheses/](https://leetcode.com/problems/valid-parentheses/)

## 题目

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
```
Input: "()"
Output: true
```

Example 2:
```
Input: "()[]{}"
Output: true
```

Example 3:
```
Input: "(]"
Output: false
```

Example 4:
```
Input: "([)]"
Output: false
```

Example 5:
```
Input: "{[]}"
Output: true
```
Accepted 899,288 Submissions 2,353,413


## 问题描述
简单的括号匹配问题


## 题目分析
简单的栈的应用，没啥好说的


## 代码实现

```python
# -*- coding: utf-8 -*-


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)
        while low < high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            if nums[mid] < nums[low]:
                if target < nums[mid] or target >= nums[low]:
                    high = mid
                else:
                    low = mid + 1
            elif nums[mid] > nums[high - 1]:
                if target > nums[mid] or target < nums[low]:
                    low = mid + 1
                else:
                    high = mid
            else:
                if target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid
        return -1


if __name__ == '__main__':
    solution = Solution()
    nums = [8, 1, 2, 3, 4, 5, 6, 7]
    target = 6
    assert solution.search(nums, target) == 6

```



## 运行结果

| Time Submitted | Status                                   | Runtime | Memory | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	32 ms	| 13.8 MB	| python3|

Runtime: 32 ms, faster than 32.91% of Python3 online submissions for Valid Parentheses.
Memory Usage: 13.8 MB, less than 5.22% of Python3 online submissions for Valid Parentheses.