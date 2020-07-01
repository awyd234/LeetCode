class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        for index, each_data in enumerate(nums):
            if each_data == 0:
                zero_count += 1
                continue
            nums[index - zero_count] = each_data
        start = len(nums) - zero_count
        while start < len(nums):
            nums[start] = 0
            start += 1


if __name__ == '__main__':
    solution = Solution()
    this_input = list()
    this_input.append([[0, 1, 0, 3, 12], [1, 3, 12, 0, 0]])
    for each_value in this_input:
        solution.moveZeroes(each_value[0])
        assert each_value[0] == each_value[1]
