# Time = O(1)
# Space = O(1)

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x == 0:
            return True
        if x % 10 == 0:
            return False

        originalNum = x
        numReversed = 0

        while x > 0:
            lastDigit = x % 10
            numReversed = numReversed * 10 + lastDigit
            x = x // 10
        return numReversed == originalNum