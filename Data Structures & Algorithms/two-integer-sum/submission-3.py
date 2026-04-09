class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicts = {}

        for i in range(len(nums)):
            dicts[nums[i]] = i
        

        for j, n in enumerate(nums):
            diff = target - n
            if diff in dicts and dicts[diff] !=j:
                return [j, dicts[diff]]
            
        
    