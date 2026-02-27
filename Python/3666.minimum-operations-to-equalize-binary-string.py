# Time = O(n)
# Space = O(1)

class Solution(object):
    def minOperations(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        zero = s.count('0')
        for i in xrange(len(s)+1):
            if (i*k-zero)&1:
                continue
            if i&1:
                if zero <= i*k <= zero*i+(len(s)-zero)*(i-1):
                    return i
            else:
                if zero <= i*k <= zero*(i-1)+(len(s)-zero)*i:
                    return i
        return -1