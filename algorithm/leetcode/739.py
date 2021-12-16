# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         n = len(temperatures)
#         hottest = 0
#         answer = [0] * n
#
#         for curr_day in range(n - 1, -1, -1):
#             current_temp = temperatures[curr_day]
#             if current_temp >= hottest:
#                 hottest = current_temp
#                 continue
#
#             days = 1
#             while temperatures[curr_day + days] <= current_temp:
#                 days += answer[curr_day + days]
#             answer[curr_day] = days
#
#         return answer

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i, cur in enumerate(temperatures):
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)

        return answer


# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         answer = []
#         for i in range(len(temperatures)):
#             cnt = 0
#             for j in range(i + 1, len(temperatures)):
#                 cnt += 1
#                 if temperatures[j] > temperatures[i]:
#                     answer.append(cnt)
#                     break
#             else:
#                 answer.append(0)
#         print(answer)




