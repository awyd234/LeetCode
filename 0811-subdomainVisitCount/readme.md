# 811. Subdomain Visit Count

link: [https://leetcode.com/problems/subdomain-visit-count/](https://leetcode.com/problems/subdomain-visit-count/)

## Difficulty
Easy

## 题目

A website domain like "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com", and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.

Now, call a "count-paired domain" to be a count (representing the number of visits this domain received), followed by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com".

We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains, (in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.
```
Example 1:
Input: 
["9001 discuss.leetcode.com"]
Output: 
["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
Explanation: 
We only have one website domain: "discuss.leetcode.com". As discussed above, the subdomain "leetcode.com" and "com" will also be visited. So they will all be visited 9001 times.
```
```
Example 2:
Input: 
["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
Output: 
["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
Explanation: 
We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5 times. For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.
```
Notes:

- The length of cpdomains will not exceed 100. 
- The length of each domain name will not exceed 100.
- Each address will have either 1 or 2 "." characters.
- The input count in any count-paired domain will not exceed 10000.
- The answer output can be returned in any order.
Accepted
74,889
Submissions
109,437


## 问题描述
统计各级域名出现的次数

## 题目分析
建立一个大map，对每个域名进行多级切分，然后统计计数


## 代码实现

```python
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count_dict = {}
        for each_item in cpdomains:
            count, address_origin = each_item.split(' ')
            address_list = address_origin.split('.')
            for each_index in range(len(address_list)):
                this_address = '.'.join(address_list[each_index:])
                if count_dict.get(this_address) is None:
                    count_dict[this_address] = 0
                count_dict[this_address] += int(count)
        return ['%d %s' % (count, sub_domain) for sub_domain, count in count_dict.items()]
```



## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 	52 ms	| 13.8 MB		| python3|

Runtime: 52 ms, faster than 72.83% of Python3 online submissions for Subdomain Visit Count.
Memory Usage: 13.8 MB, less than 8.33% of Python3 online submissions for Subdomain Visit Count.
