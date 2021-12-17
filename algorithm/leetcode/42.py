from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        lt, rt = 0, len(height)-1
        lt_high = height[lt]
        rt_high = height[rt]

        answer = 0
        while lt < rt:
            if lt_high <= rt_high:
                lt += 1
                lt_high = max(lt_high, height[lt])
                answer += lt_high - height[lt]
            else:
                rt -= 1
                rt_high = max(rt_high, height[rt])
                answer += rt_high - height[rt]
        return answer


# class Solution:
#     def trap(self, height: List[int]) -> int:
#         stack = []
#         answer = 0
#
#         for i in range(len(height)):
#             # 변곡점을 만나는 경우
#             while stack and height[i] > height[stack[-1]]:
#                 # 스택에서 꺼낸다
#                 top = stack.pop()
#
#                 if not len(stack):
#                     print(i, len(stack), 'not len stack')
#                     break
#
#                 # 이전과의 차이만큼 물 높이 처리
#                 dis = i - stack[-1] - 1
#                 waters = min(height[i], height[stack[-1]]) - height[top]
#
#                 answer += dis * waters
#
#             stack.append(i)
#             print(stack)
#         return answer


# class Solution:
#     def trap(self, height: List[int]) -> int:
#         # 예외 처리
#         if not height:
#             return 0
#
#         answer = 0
#         lt, rt = 0, len(height)-1
#         lt_max, rt_max = height[lt], height[rt]
#         while lt < rt:
#             lt_max, rt_max = max(lt_max, height[lt]), max(rt_max, height[rt])
#             # 더 높은쪽을 향해 투포인터 이동
#             if lt_max <= rt_max:
#                 answer += lt_max - height[lt]
#                 lt += 1
#             else:
#                 answer += rt_max - height[rt]
#                 rt -= 1
#         return answer


print(Solution.trap('',[0,1,0,2,1,0,1,3,2,1,2,1]))