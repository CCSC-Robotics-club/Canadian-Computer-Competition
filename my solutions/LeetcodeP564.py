'''
给定一个表示整数的字符串 n ，返回与它最近的回文整数（不包括自身）。如果不止一个，返回较小的那个。

“最近的”定义为两个整数差的绝对值最小。

 

示例 1:

输入: n = "123"
输出: "121"
示例 2:

输入: n = "1"
输出: "0"
解释: 0 和 2是最近的回文，但我们返回最小的，也就是 0。


思路：
把字符串从中间切开，左边的部分原封不动，右边的部分变成左边镜像，这么做是因为越靠右的字符位数越小，改变他们不会让数字对比原数字有太大变化
如果本来就是回文，直接变中间的数字，因为如果变两边的必须得对称变，这样和原数字差就会很大
'''

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if len(n) == 1:
            if n == 1:
                return 2
            return int(n) - 1
        if len(n)%2==0:
            first_half = n[0:len(n)/2+1]
            second_half = ""
            for i in range(len(first_half)-1, -1,-1):
                second_half += first_half[i]
            return second_half + first_half
        first_half = n[0:int(len(n)/2)]
        second_half = ""
        for i in range(len(first_half)-1, -1, -1):
            second_half += first_half[i]
        return first_half += n[int(len(n)/2)] + second_half
        
