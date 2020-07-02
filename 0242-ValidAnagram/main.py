from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__ == '__main__':
    solution = Solution()
    this_input = list()
    this_input.append(["anagram", "nagaram", True])
    this_input.append(["rat", "car", False])
    for each_value in this_input:
        assert solution.isAnagram(each_value[0], each_value[1]) == each_value[2]
