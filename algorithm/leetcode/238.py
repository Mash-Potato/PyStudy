from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        p = 1
        for i in range(len(nums)):
            answer.append(p)
            p *= nums[i]

        p = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= p
            p *= nums[i]

        return answer

print(Solution.productExceptSelf('', [1,2,3,4]))


# test
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         answer = [1] * len(nums)
#         answer2 = [1] * len(nums)
#
#         for i in range(1, len(nums)):
#             answer[i] = answer[i-1] * nums[i-1]
#
#         for i in range(len(nums)-2, -1, -1):
#             answer2[i] = answer2[i+1] * nums[i+1]
#
#         for i in range(len(nums)):
#             answer[i] *= answer2[i]
#
#         return answer
