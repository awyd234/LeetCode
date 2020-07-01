class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        if n == 2:
            return 0
        result = [True] * n
        result[1] = False
        result[2] = True
        for each_num in range(2, int(n ** 0.5) + 1):
            this_index = 2
            if not result[each_num]:
                continue
            while this_index * each_num < n:
                result[this_index * each_num] = False
                this_index += 1
        count = 0
        for each_data in range(2, n):
            if result[each_data]:
                count += 1
        return count


if __name__ == '__main__':
    solution = Solution()
    this_input = list()
    this_input.append([10, 4])
    this_input.append([0, 0])
    this_input.append([1, 0])
    this_input.append([2, 0])
    this_input.append([3, 1])
    for each_value in this_input:
        assert solution.countPrimes(each_value[0]) == each_value[1]
