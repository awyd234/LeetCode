# 200. Number of Islands

link: [https://leetcode.com/problems/number-of-islands/](https://leetcode.com/problems/number-of-islands/)

## Difficulty
Medium

## 题目

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


Example 1:
```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

Example 2:
```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

Accepted
734,651

Submissions
1,579,538

## 问题描述
找出矩阵中被0所包围的1的块的个数

## 题目分析
从每个元素开始去遍历，记录元素的访问状态，如果元素是1，且未被访问，则对其BFS，找出对应块中的所有1，这里效率应该是可以持续优化的，这种做法实际还是有很多重复判断

## 代码实现

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        row_length = len(grid)
        if row_length == 0:
            return 0
        col_length = len(grid[0])
        visited_list = [False] * row_length * col_length
        for row_index, row_list in enumerate(grid):
            for col_index, data in enumerate(row_list):
                if data == '0':
                    continue
                if visited_list[row_index * col_length + col_index]:
                    continue
                count += 1
                this_queue = [(row_index, col_index)]
                while len(this_queue) != 0:
                    this_row, this_col = this_queue.pop(0)
                    if this_row >= row_length or this_row < 0:
                        continue
                    if this_col >= col_length or this_col < 0:
                        continue
                    this_data = grid[this_row][this_col]
                    if this_data == '0':
                        continue
                    if visited_list[this_row * col_length + this_col]: 
                        continue
                    visited_list[this_row * col_length + this_col] = True
                    this_queue.append([this_row - 1, this_col])
                    this_queue.append([this_row, this_col - 1])
                    this_queue.append([this_row + 1, this_col])
                    this_queue.append([this_row, this_col + 1])
        return count
```

## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 		180 ms	| 14.8 MB		| python3|


Runtime: 180 ms, faster than 33.97% of Python3 online submissions for Number of Islands.

Memory Usage: 14.8 MB, less than 75.70% of Python3 online submissions for Number of Islands.