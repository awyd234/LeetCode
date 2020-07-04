class Solution:
    def intersection(self, nums1: list, nums2: list) -> list:
        # result_list = []
        # result_set = set()
        # nums1_set = set(nums1)
        # nums2_set = set(nums2)
        # for each_data in nums1_set:
        #     if each_data in nums2_set and each_data not in result_set:
        #         result_list.append(each_data)
        #         result_set.add(each_data)
        # return result_list
        return list(set(nums1).intersection(set(nums2)))


if __name__ == '__main__':
    solution = Solution()
    this_input = list()
    this_input.append([[1, 2, 2, 1], [2, 2], [2]])
    this_input.append([[4, 9, 5], [9, 4, 9, 8, 4], [9, 4]])
    for each_value in this_input:
        assert set(solution.intersection(each_value[0], each_value[1])) == set(each_value[2])
