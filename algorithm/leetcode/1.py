from typing import List

# 키 조회 개선
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, num in enumerate(nums):
            if target - num in nums_dict:
                return [nums_dict[target - num], i]
            nums_dict[num] = i


# 키 조회
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         nums_dict = {}
#         for i, num in enumerate(nums):
#             nums_dict[num] = i
#
#         for i, num in enumerate(nums):
#             if target - num in nums_dict and i != nums_dict[target - num]:
#                 return [nums.index(num), nums_dict[target - num]]

# in 탐색
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i, v in enumerate(nums):
#             res = target - v
#             if res in nums[i+1:]:
#                 return [nums.index(v), nums[i+1:].index(res)+(i+1)]

# brute
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)-1):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

print(Solution.twoSum('', [2, 7, 11, 15], 9))
