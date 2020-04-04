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


if __name__ == '__main__':
    solution = Solution()
    this_input = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    assert solution.orangesRotting(this_input) == -1
