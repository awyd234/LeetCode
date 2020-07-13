class Solution:
    def numIslands(self, grid) -> int:
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


if __name__ == '__main__':
    solution = Solution()
    this_input = list()
    this_input.append(
        [[["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]],
         1])
    this_input.append(
        [[["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]],
         3])
    this_input.append([[], 0])
    for each_value in this_input:
        assert solution.numIslands(each_value[0]) == each_value[1]
