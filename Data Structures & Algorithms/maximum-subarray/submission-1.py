class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # for i in range(1, len(nums)):
        #     nums[i] = max(nums[i], nums[i] + nums[i-1])
        
        # return max(nums)

        res = nums[0]
        t = 0

        for i in nums:
            if t < 0:
                t = 0
            
            t += i
            res = max(res, t)
        
        return res
        