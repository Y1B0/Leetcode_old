class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = 0
        for i,n in enumerate(nums):
            if n < target:
                res = i+1
            else:
                break
        
        return res
