from typing import List

# 키 조회 개선
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_dict = {}
        for i, num in enumerate(nums):
            if target-num in n_dict:
                return [n_dict[target-num], i]
            n_dict[num] = i


# 키 조회
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         n_dict = {}
#         for i, num in enumerate(nums):
#             n_dict[num] = i
#
#         for i, num in enumerate(nums):
#             if target-num in n_dict and i != n_dict[target-num]:
#                 return [nums.index(num), n_dict[target-num]]

# in 탐색
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i, num in enumerate(nums):
#             if target - num in nums[i+1:]:
#                 return [nums.index(num), nums[i+1:].index(target-num)+(i+1)]

# brute
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)-1):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

print(Solution.twoSum('', [2, 7, 11, 15], 9))
