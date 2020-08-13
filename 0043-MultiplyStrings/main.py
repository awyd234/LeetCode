class Solution:
    def char_to_num(self, char_val):
        return ord(char_val) - ord('0')

    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        all_result = []
        for index, each_str in enumerate(num2[::-1]):
            next_val = 0
            result = ""
            each_num = self.char_to_num(each_str)
            for num1_str in num1[::-1]:
                this_result = self.char_to_num(num1_str) * each_num + next_val
                next_val = this_result // 10
                this_result %= 10
                result = str(this_result) + result
            if next_val != 0:
                result = str(next_val) + result
            for i in range(index):
                result += '0'
            all_result.append(result)
        return_result = ""
        next_val = 0
        index = 0
        while next_val != 0 or any([index < len(each_data)for each_data in all_result]):
            this_data = 0
            for each_data in all_result:
                if index < len(each_data):
                    this_data += self.char_to_num(each_data[-index - 1])
            this_data += next_val
            next_val = this_data // 10
            this_data %= 10
            return_result = str(this_data) + return_result
            index += 1
        index = 0
        while index < len(return_result) and return_result[index] == "0":
            index += 1
        if index == len(return_result):
            return_result = "0"
        else:
            return_result = return_result[index:]
        return return_result


if __name__ == '__main__':
    solution = Solution()
    this_input = list()
    this_input.append(["34123", "2232", "76162536"])
    this_input.append(["9133", "0", "0"])
    for each_value in this_input:
        assert solution.multiply(each_value[0], each_value[1]) == each_value[2]
