class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        v = [0] * n
        
        for i in range(n):
            j = n - 1
            while j >= 0 and grid[i][j] == 0:
                j -= 1
            v[i] = j
        swaps = 0
        
        for i in range(n):
            j = i
            while j < n and v[j] > i:
                j += 1
            if j == n:
                return -1
            swaps += j - i
            while j > i:
                v[j] = v[j - 1]
                j -= 1
        return swaps