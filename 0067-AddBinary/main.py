class Solution:
    def addBinary(self, a: str, b: str) -> str:
        index = 1
        to_add = 0
        result = []
        max_index = max([len(a), len(b)]) + 1
        a = '0' * (max_index - len(a)) + a
        b = '0' * (max_index - len(b)) + b
        while index <= max_index:
            int_a = int(a[-index])
            int_b = int(b[-index])
            this_add = int_a + int_b + to_add
            if this_add > 1:
                to_add = 1
                this_add = this_add - 2
            else:
                to_add = 0
            result.append(this_add)
            index += 1
        result.append(to_add)
        result.reverse()
        start_index = 0
        while len(result) > start_index and result[start_index] == 0:
            start_index += 1
        result = ''.join([str(_) for _ in result[start_index:]])
        if result == '':
            result = '0'
        return result


if __name__ == '__main__':
    solution = Solution()
    this_input = list()
    this_input.append(("0", "0", "0"))
    this_input.append(("111", "111",  "1110"))
    this_input.append(("110", "11", "1001"))
    for each_value in this_input:
        assert solution.addBinary(each_value[0], each_value[1]) == each_value[2]
