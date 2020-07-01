class Solution:
    def climbStairs(self, n: int) -> int:
        result_list = [0] * (n + 1)
        for index in range(1, n + 1):
            if index == 1:
                result_list[index] = 1
            elif index == 2:
                result_list[index] = 2
            else:
                result_list[index] = result_list[index - 1] + result_list[index - 2]
        return result_list[n]


if __name__ == '__main__':
    solution = Solution()
    this_input = list()
    this_input.append([2, 2])
    this_input.append([3, 3])
    for each_value in this_input:
        assert solution.climbStairs(each_value[0]) == each_value[1]
