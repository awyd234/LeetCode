class Solution:
    def isPalindrome(self, s: str) -> bool:
        head = 0
        tail = len(s) - 1
        while tail >= 0:
            while not (s[head].isdigit() or s[head].isalpha()):
                head += 1
                if head >= tail:
                    return True
            while not (s[tail].isdigit() or s[tail].isalpha()):
                tail -= 1
                if tail <= head:
                    return True
            if s[head].lower() != s[tail].lower():
                return False
            head += 1
            tail -= 1
        return True


if __name__ == '__main__':
    solution = Solution()
    input1 = (".a", True)
    input2 = ("A man, a plan, a canal: Panama", True)
    input3 = ("", True)
    assert solution.isPalindrome(input1[0]) == input1[1]
    assert solution.isPalindrome(input2[0]) == input2[1]
    assert solution.isPalindrome(input3[0]) == input3[1]
