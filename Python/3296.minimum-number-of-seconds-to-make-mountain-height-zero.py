class Solution(object):
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        """
        :type mountainHeight: int
        :type workerTimes: List[int]
        :rtype: int
        """
        min_heap = [(0+1*t, i, 1) for i, t in enumerate(workerTimes)]
        heapq.heapify(min_heap)
        for _ in xrange(mountainHeight):
            result, i, x = heapq.heappop(min_heap)
            heapq.heappush(min_heap, (result+(x+1)*workerTimes[i], i, x+1))
        return result