class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters_list = []
        letters_dict = {}
        for index, each_str in enumerate(s):
            if each_str not in letters_dict:
                letters_dict[each_str] = 0
                letters_list.append([each_str, index])
            letters_dict[each_str] += 1
        for each_str, index in letters_list:
            if letters_dict.get(each_str) == 1:
                return index
        return -1


if __name__ == '__main__':
    solution = Solution()
    this_input = list()
    this_input.append(['leetcode', 0])
    this_input.append(['loveleetcode', 2])
    this_input.append(['leetleet', -1])
    for each_value in this_input:
        assert solution.firstUniqChar(each_value[0]) == each_value[1]
