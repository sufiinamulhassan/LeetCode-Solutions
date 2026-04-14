class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        """
        :type robot: List[int]
        :type factory: List[List[int]]
        :rtype: int
        """
        robot.sort(), factory.sort()
        dp = [float("inf")]*(len(robot)+1)  
        dp[0] = 0
        for i in xrange(len(factory)):
            prefix = 0
            dq = collections.deque([(dp[0]-prefix, 0)])  
            for j in xrange(1, len(robot)+1):
                prefix += abs(robot[j-1]-factory[i][0])
                if j-dq[0][1] == factory[i][1]+1:
                    dq.popleft()
                while dq and dq[-1][0] >= dp[j]-prefix:
                    dq.pop()
                dq.append((dp[j]-prefix, j))
                dp[j] = dq[0][0]+prefix
        return dp[-1]