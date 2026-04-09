# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         res = 0
#         farthest = 0

#         for i in range(len(nums)-1):
#             if i > farthest:
#                 return -1

#             if i +nums[i] > farthest:
#                 farthest = i +nums[i]
#                 res += 1
            
#             if farthest >= len(nums) - 1:
#                 return res
        
#         return res

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        farthest = 0
        current_end = 0

        for i in range(n - 1):  # don't need to jump from last index
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps
            


        