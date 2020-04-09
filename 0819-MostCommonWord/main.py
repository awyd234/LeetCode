class Solution:
    def mostCommonWord(self, paragraph: str, banned) -> str:
        symbol_list = list("!?',;.")
        for each_symbol in symbol_list:
            paragraph = paragraph.replace(each_symbol, ' ')
        paragraph_list = [_ for _ in paragraph.split(' ') if _.strip() != '']
        banned_set = set(banned)
        word_count_dict = {}
        result_word = ""
        max_count = 0
        for each_word in paragraph_list:
            each_word = each_word.lower()
            if each_word in banned_set:
                continue
            if word_count_dict.get(each_word) is None:
                word_count_dict[each_word] = 0
            word_count_dict[each_word] += 1
            if word_count_dict[each_word] > max_count:
                max_count = word_count_dict[each_word]
                result_word = each_word
        return result_word
