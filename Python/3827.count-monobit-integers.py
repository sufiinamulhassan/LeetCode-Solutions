# Time: O(n * log n)

class Solution(object):
    def countMonobit(self, n):
        return sum(len(set(bin(i)[2:])) == 1 for i in range(n + 1))