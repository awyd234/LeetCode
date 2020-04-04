# 994. Rotting Oranges

link: [https://leetcode.com/problems/rotting-oranges/](https://leetcode.com/problems/rotting-oranges/)

## Difficulty
Easy

## 题目

In a given grid, each cell can have one of three values:

- the value 0 representing an empty cell;
- the value 1 representing a fresh orange;
- the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.


Example 1:

![image1](image1.png)
```
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
```

Note:

- 1. 1 <= grid.length <= 10
- 2. 1 <= grid[0].length <= 10
- 3. grid[i][j] is only 0, 1, or 2.


## 问题描述
简单的应用题，每一分钟向四周扩散

## 题目分析
最简单的方法就是模拟实验结果，有种更快的方法是使用BFS，建立队列来做


## 代码实现

```python
class Solution:
    def orangesRotting(self, grid) -> int:
        flag = True
        cost = 0
        while flag:
            flag = False
            this_set = set()
            for each_col_index, each_row_list in enumerate(grid):
                for each_row_index, each_item in enumerate(each_row_list):
                    if each_item == 3:
                        if (each_col_index, each_row_index) not in this_set:
                            grid[each_col_index][each_row_index] = 2
                    if grid[each_col_index][each_row_index] == 2:
                        if each_col_index > 0:
                            if grid[each_col_index - 1][each_row_index] == 1:
                                grid[each_col_index - 1][each_row_index] = 3
                                this_set.add((each_col_index - 1, each_row_index))
                                flag = True
                        if each_col_index + 1 < len(grid):
                            if grid[each_col_index + 1][each_row_index] == 1:
                                grid[each_col_index + 1][each_row_index] = 3
                                this_set.add((each_col_index + 1, each_row_index))
                                flag = True
                        if each_row_index > 0:
                            if grid[each_col_index][each_row_index - 1] == 1:
                                grid[each_col_index][each_row_index - 1] = 3
                                this_set.add((each_col_index, each_row_index - 1))
                                flag = True
                        if each_row_index + 1 < len(each_row_list):
                            if grid[each_col_index][each_row_index + 1] == 1:
                                grid[each_col_index][each_row_index + 1] = 3
                                this_set.add((each_col_index, each_row_index + 1))
                                flag = True
            if flag:
                cost += 1
        for each_col_index, each_row_list in enumerate(grid):
            for each_row_index, each_item in enumerate(each_row_list):
                if each_item == 1:
                    return -1
        return cost
```



## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 60 ms	| 13.7 MB	| python3|

Runtime: 60 ms, faster than 18.95% of Python3 online submissions for Rotting Oranges.
Memory Usage: 13.7 MB, less than 16.67% of Python3 online submissions for Rotting Oranges.