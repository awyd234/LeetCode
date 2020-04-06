class Solution:
    def isAlienSorted(self, words, order: str) -> bool:
        weight_dict = {letter: index for index, letter in enumerate(order)}
        for word_index in range(len(words) - 1):
            first_word = words[word_index]
            next_word = words[word_index + 1]
            if first_word == next_word:
                continue
            min_length = min([len(first_word), len(next_word)])
            for letter_index in range(min_length):
                if weight_dict[first_word[letter_index]] > weight_dict[next_word[letter_index]]:
                    return False
                elif weight_dict[first_word[letter_index]] < weight_dict[next_word[letter_index]]:
                    break
            if len(first_word) > len(next_word) and first_word[: min_length] == next_word:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    this_input1 = (["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz")
    assert solution.isAlienSorted(this_input1[0], this_input1[1]) == True
