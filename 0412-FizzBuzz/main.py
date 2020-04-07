import operator


class Solution:
    def fizzBuzz(self, n: int) -> list:
        result_list = []
        for index in range(1, n + 1):
            if index % 15 == 0:
                result_list.append('FizzBuzz')
            elif index % 3 == 0:
                result_list.append('Fizz')
            elif index % 5 == 0:
                result_list.append('Buzz')
            else:
                result_list.append(str(index))
        return result_list
