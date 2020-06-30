class Solution:
    flag = True

    def validPalindrome(self, s: str) -> bool:
        first_index = 0
        last_index = len(s) - 1
        while first_index < last_index:
            if s[first_index] == s[last_index]:
                first_index += 1
                last_index -= 1
                continue
            if self.flag:
                self.flag = False
                return self.validPalindrome(s[first_index + 1: last_index + 1]) or self.validPalindrome(
                    s[first_index: last_index])
            else:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    this_input = list()
    this_input.append(("aba", True))
    this_input.append(("abca", True))
    this_input.append(("abcda", False))
    for each_value in this_input:
        assert solution.validPalindrome(each_value[0]) == each_value[1]
