'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.
'''


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ans = 0
        xor_result = x ^ y
        while xor_result > 0:
            if xor_result % 2 == 1:
                ans += 1
            xor_result >>= 1
        return ans
