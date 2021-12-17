class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        # 스택에 인덱스 추가
        stack = []
        for index, c_t in enumerate(temperatures):
            while stack and c_t > temperatures[stack[-1]]:
                day = stack.pop()
                answer[day] = index - day
            stack.append(index)

        return answer
    
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


# my code 시간초과
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




