class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        final_result = 0
        origin_result = x
        while x > 0:
            final_result *= 10
            final_result += (x % 10)
            x //= 10
        if final_result == origin_result:
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    this_input = list()
    this_input.append([121, True])
    this_input.append([-121, False])
    this_input.append([10, False])
    for each_value in this_input:
        assert solution.isPalindrome(each_value[0]) == each_value[1]
