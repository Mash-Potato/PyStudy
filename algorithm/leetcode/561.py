class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

# class Solution:
#     def arrayPairSum(self, nums: List[int]) -> int:
#         nums.sort()
#         return sum(nums[0:len(nums):2])
