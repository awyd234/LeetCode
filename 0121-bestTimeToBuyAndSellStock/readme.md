# 121. Best Time to Buy and Sell Stock

link: [https://leetcode.com/problems/best-time-to-buy-and-sell-stock/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

## Difficulty
Easy

## 题目

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:
```
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
```
Example 2:
```
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

Accepted 761,425, Submissions 1,534,190


## 问题描述
股票买卖问题，即找出一段距离，终点离起点的距离最大

## 题目分析
最简单的方法是暴力搜索，那样复杂度是$O(n^2)$，会超时，只需要设置两个变量，从头完全遍历一遍即可，并持续更新买点和卖点


## 其它方法
可以考虑动态规划，此外可能可以尝试二分搜索分而治之来做


## 代码实现

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        buy = float("inf")
        for price in prices:
            buy = min([buy, price])
            output = max([output, price - buy])
        return output
```



## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 68 ms	| 15.1 MB		| python3|

Runtime: 68 ms, faster than 34.89% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 15.1 MB, less than 5.75% of Python3 online submissions for Best Time to Buy and Sell Stock.