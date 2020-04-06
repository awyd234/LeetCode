class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        num1_list = list(num1)
        num2_list = list(num2)
        the_next = 0
        for each_index in range(1, len(num1_list) + 1):
            number1 = num1_list[-each_index]
            if each_index > len(num2_list):
                number2 = '0'
            else:
                number2 = num2_list[-each_index]
            this_num = ord(number1) + ord(number2) - 2 * ord('0') + the_next
            num1_list[-each_index] = chr(this_num % 10 + ord('0'))
            the_next = this_num // 10
        output = ''.join(num1_list)
        if the_next != 0:
            output = chr(the_next + ord('0')) + output
        return output


if __name__ == '__main__':
    solution = Solution()
    this_input1 = ("256", "13", "269")
    this_input2 = ("13", "99", "112")
    assert solution.addStrings(this_input1[0], this_input1[1]) == this_input1[2]
    assert solution.addStrings(this_input2[0], this_input2[1]) == this_input2[2]
