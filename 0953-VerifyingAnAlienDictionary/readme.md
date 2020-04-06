# 953. Verifying an Alien Dictionary

link: [https://leetcode.com/problems/verifying-an-alien-dictionary/](https://leetcode.com/problems/verifying-an-alien-dictionary/)

## Difficulty
Easy

## 题目

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

Example 1:
```
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
```
Example 2:
```
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
```
Example 3:
```
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
```

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 20
- order.length == 26
- All characters in words[i] and order are English lowercase letters.
Accepted
79,311
Submissions
144,446


## 问题描述
指定权重系数和规则，判断一个list的排序是否符合规范

## 题目分析
建立一个map映射各字母权重，注意各种极端情况和边界情况


## 代码实现

```python
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
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
```



## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 	24 ms	| 13.9 MB		| python3|

Runtime: 24 ms, faster than 98.80% of Python3 online submissions for Verifying an Alien Dictionary.
Memory Usage: 13.9 MB, less than 5.55% of Python3 online submissions for Verifying an Alien Dictionary.
