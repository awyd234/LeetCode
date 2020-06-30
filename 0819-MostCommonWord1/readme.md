# 819. Most Common Word

link: [https://leetcode.com/problems/most-common-word/](https://leetcode.com/problems/most-common-word/)

## Difficulty
Easy

## 题目

Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

 
Example:
```
Input: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
```

Note:

- 1 <= paragraph.length <= 1000.
- 0 <= banned.length <= 100.
- 1 <= banned[i].length <= 10.
- The answer is unique, and written in lowercase (even if its occurrences in paragraph may have uppercase symbols, and even if it is a proper noun.)
- paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
- There are no hyphens or hyphenated words.
- Words only consist of letters, never apostrophes or other punctuation symbols.

Accepted
124,767
Submissions
284,113

## 问题描述
给定一个banned的list，遍历字符串中，找到最常出现的单词，忽略大小写

## 题目分析
没啥好说的，只不过不用排序，只取最大一个，那拿一个变量保存即可


## 代码实现

```python
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
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
```



## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 		32 ms	| 13.9 MB		| python3|

Runtime: 32 ms, faster than 70.15% of Python3 online submissions for Most Common Word.
Memory Usage: 13.9 MB, less than 5.88% of Python3 online submissions for Most Common Word.