class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            ind = (l + r) // 2
            n = nums[ind]

            if n == target:
                return ind
            
            elif n > target:
                r = ind - 1
            
            else:
                l = ind + 1
        
        return -1
        
        