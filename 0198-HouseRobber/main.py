from collections import Counter


class Solution:

    def rob(self, nums) -> int:
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
            rob_nums.append(
                max([rob_nums[each_index], rob_nums[each_index - 1] + each_data, rob_nums[each_index - 2] + each_data]))
        return rob_nums[-1]


if __name__ == '__main__':
    solution = Solution()
    this_input = list()
    this_input.append([[1, 2, 3, 1], 4])
    this_input.append([[2, 7, 9, 3, 1], 12])
    this_input.append([[2], 2])
    this_input.append([[2, 3], 3])
    this_input.append([[2, 3, 5], 7])
    for each_value in this_input:
        assert solution.rob(each_value[0]) == each_value[1]
