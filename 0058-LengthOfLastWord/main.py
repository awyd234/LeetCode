class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # all_list = s.split()
        # if len(all_list) == 0:
        #     return 0
        # return len(all_list[-1])
        index = 0
        count = len(s)
        while count >= 1 and s[count - 1] == " ":
            count -= 1
        if count == 0:
            return 0
        for each_data in s[count - 1::-1]:
            if each_data == " ":
                break
            index += 1
        return index


if __name__ == '__main__':
    solution = Solution()
    this_input = list()
    this_input.append(["Hello World", 5])
    this_input.append(["aaa ", 3])
    this_input.append([" ", 0])
    this_input.append(["", 0])
    for each_value in this_input:
        assert solution.lengthOfLastWord(each_value[0]) == each_value[1]
