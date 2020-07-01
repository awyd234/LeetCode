# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

compare_data = 0


def isBadVersion(mid):
    return mid >= compare_data


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n
        while low < high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return low


if __name__ == '__main__':
    solution = Solution()
    this_input = list()
    this_input.append([5, 4])
    this_input.append([10, 3])
    for each_value in this_input:
        compare_data = each_value[1]
        assert solution.firstBadVersion(each_value[0]) == each_value[1]
