class Solution:
    def longestCommonPrefix(self, strs) -> str:
        result = ""
        max_length = min([len(_) for _ in strs]) if len(strs) != 0 else 0
        for index in range(max_length):
            if all([_[index] == strs[0][index] for _ in strs[1:]]):
                result += strs[0][index]
            else:
                break
        return result


if __name__ == '__main__':
    solution = Solution()
    this_input = list()
    this_input.append([["aca", "cba"], ""])
    this_input.append([["flower", "flow", "flight"], "fl"])
    this_input.append([[], ""])
    for each_value in this_input:
        assert solution.longestCommonPrefix(each_value[0]) == each_value[1]
