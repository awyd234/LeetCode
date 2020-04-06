class Solution:
    def reverse_interger(self, x: int) -> int:
        x_list = []
        negtive = 1
        if x < 0:
            negtive = -1
            x = -x
        while x > 0:
            x_list.append(x % 10)
            x //= 10
        output = 0
        coefficient = 1
        for each_index, each_num in enumerate(x_list[::-1]):
            output += each_num * coefficient
            coefficient *= 10
        output *= negtive
        if output >= 2 ** 31 or output < -2 ** 31:
            output = 0
        return output


if __name__ == '__main__':
    solution = Solution()
    this_input = list()
    this_input.append((123, 321))
    this_input.append((-123, -321))
    this_input.append((1534236469, 0))
    for each_value in this_input:
        assert solution.reverse_interger(each_value[0]) == each_value[1]
