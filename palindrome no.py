Palindrome Number
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

output:-

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        lis = []
        while x >= 10:
            lis.append(x % 10)
            x //= 10
        lis.append(x)
        for i in range(int(math.ceil(len(lis)/2))):
            if lis[i] != lis[len(lis)-i-1]:
                return False
        return True
