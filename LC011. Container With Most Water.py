class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left,right = 0,len(height)-1
        area = 0
        while right > left:
            if min(height[left],height[right])*(right-left) > area:
                area = min(height[left],height[right])*(right-left)
            if height[right]>height[left]:
                left += 1
            else:
                right -= 1
        return area
    
s = Solution()
print(s.maxArea([1,4,4,3]))
