class Solution:
    def maxProfit(self, prices) -> int:
        output = 0
        buy = float("inf")
        for price in prices:
            buy = min([buy, price])
            output = max([output, price - buy])
        return output


if __name__ == '__main__':
    solution = Solution()
    this_input1 = [7, 1, 5, 3, 6, 4]
    this_input2 = [7, 6, 4, 3, 1]
    assert solution.maxProfit(this_input1) == 5
    assert solution.maxProfit(this_input2) == 0
