# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def minRemoval(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        
        max_el = nums[0]
        min_el = nums[0]
        
        L = 1
        i = 0
        j = 0
        
        while j < n:
            max_el = nums[j]
            min_el = nums[i]
            
            while i < j and max_el > k * min_el:
                i += 1
                min_el = nums[i]
            
            L = max(L, j - i + 1)
            j += 1
        
        return n - L