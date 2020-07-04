class Solution:
    def missingNumber(self, nums: list) -> int:
        len_nums = len(nums)
        return len_nums * (len_nums + 1) // 2 - sum(nums)


if __name__ == '__main__':
    solution = Solution()
    this_input = list()
    this_input.append([[3, 0, 1], 2])
    for each_value in this_input:
        assert solution.missingNumber(each_value[0]) == each_value[1]
