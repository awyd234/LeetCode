class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s_len = len(s)
        for index in range(s_len // 2):
            s[index], s[s_len - index - 1] = s[s_len - index - 1], s[index]


if __name__ == '__main__':
    solution = Solution()
    this_input = list()
    this_input.append([["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]])
    this_input.append([["h", "a"], ["a", "h"]])
    this_input.append([["h", "a", "b"], ["b", "a", "h"]])
    this_input.append([["h"], ["h"]])
    for each_value in this_input:
        solution.reverseString(each_value[0])
        assert each_value[0] == each_value[1]
