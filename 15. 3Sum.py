class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l < r:
                s = nums[i]+nums[l]+nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    comb = [nums[i],nums[l],nums[r]]
                    if not comb in res:
                        res.append(comb)
                        
                    l += 1
                    r -= 1
        return res

s = Solution()
print s.threeSum([-1,0,1,2,-1,-4])