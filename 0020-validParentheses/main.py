class Solution:
    def isValid(self, s: str) -> bool:
        total_list = list()

        map_dict = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for each_item in s:
            if len(total_list) == 0:
                total_list.append(each_item)
            else:
                map_str = map_dict.get(each_item)
                if map_str is None:
                    total_list.append(each_item)
                else:
                    top = total_list.pop()
                    if map_str != top:
                        return False
        if len(total_list) != 0:
            return False
        return True


if __name__ == '__main__':
    solution = Solution()
    this_input = '(())[][[]]]'
    target = False
    assert solution.isValid(this_input) == target