# Time:  O(n * (a + n))), a = len(set(s))
# Space: O(a)

import collections


# freq table
class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in xrange(len(s)):
            cnt = collections.defaultdict(int)
            mx = 0
            for j in xrange(i, len(s)):
                cnt[s[j]] += 1
                mx = max(mx, cnt[s[j]])
                if (j-i+1)%len(cnt) == 0 and (j-i+1)//len(cnt) == mx:
                    result = max(result, j-i+1)
        return result