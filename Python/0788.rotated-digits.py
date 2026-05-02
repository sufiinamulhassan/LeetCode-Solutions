class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        A = map(int, str(N))
        invalid, diff = set([3, 4, 7]), set([2, 5, 6, 9])
        def dp(A, i, is_prefix_equal, is_good, lookup):
            if i == len(A): return int(is_good)
            if (i, is_prefix_equal, is_good) not in lookup:
                result = 0
                for d in xrange(A[i]+1 if is_prefix_equal else 10):
                    if d in invalid: continue
                    result += dp(A, i+1,
                                 is_prefix_equal and d == A[i],
                                 is_good or d in diff,
                                 lookup)
                lookup[i, is_prefix_equal, is_good] = result
            return lookup[i, is_prefix_equal, is_good]

        lookup = {}
        return dp(A, 0, True, False, lookup)
