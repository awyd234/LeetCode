class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_value_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        this_stack = []
        result = 0
        for each_str in s:
            if len(this_stack) == 0:
                this_stack.append(each_str)
            elif isinstance(this_stack[-1], int):
                if symbol_value_dict[each_str] > this_stack[-1]:
                    this_stack.append(symbol_value_dict[each_str] - this_stack.pop())
                else:
                    result += this_stack.pop()
                    this_stack.append(each_str)
            elif symbol_value_dict[this_stack[-1]] > symbol_value_dict[each_str]:
                result += symbol_value_dict[this_stack.pop()]
                this_stack.append(each_str)
            elif symbol_value_dict[this_stack[-1]] < symbol_value_dict[each_str]:
                top_data = symbol_value_dict[this_stack.pop()]
                now_data = symbol_value_dict[each_str]
                data = now_data - top_data
                this_stack.append(data)
            else:
                this_stack.append(each_str)
            # print(result, this_stack, each_str)
        # print(this_stack)
        for each_data in this_stack:
            if isinstance(each_data, int):
                result += each_data
            else:
                result += symbol_value_dict[each_data]
        return result


if __name__ == '__main__':
    solution = Solution()
    input1 = ("MCMXCIV", 1994)
    assert solution.romanToInt(input1[0]) == input1[1]
