import operator


class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num1_index = m - 1
        num2_index = n - 1
        new_num1_index = m + n - 1
        while num1_index >= 0 and num2_index >= 0:
            if nums1[num1_index] > nums2[num2_index]:
                nums1[new_num1_index] = nums1[num1_index]
                num1_index -= 1
            else:
                nums1[new_num1_index] = nums2[num2_index]
                num2_index -= 1
            new_num1_index -= 1
        while num2_index >= 0:
            nums1[num2_index] = nums2[num2_index]
            num2_index -= 1


if __name__ == '__main__':
    solution = Solution()
    this_input1 = ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6])
    solution.merge(this_input1[0], this_input1[1], this_input1[2], this_input1[3])
    assert this_input1[0] == this_input1[4]
