class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 팰린드롬 판별 및 투 포인터 확장
        def expand(lt: int, rt: int) -> str:
            while lt >= 0 and rt <= len(s) and s[lt] == s[rt - 1]:
                lt -= 1
                rt += 1

            return s[lt + 1:rt - 1]

        # 해당 사항이 없을 때 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s

        answer = ''
        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(s)-1):
            answer = max(answer, expand(i, i+1), expand(i, i+2), key=len)
        return answer




# my code
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         lt = 0
#         rt = 1
#         l = 0
#         answer = ''
#         for lt in range(len(s)):
#             for rt in range(len(s)):
#                 tmp = s[lt:rt]
#                 if Solution.is_check(' ', tmp):
#                     if len(tmp) > l:
#                         l = len(tmp)
#                         answer = tmp
#
#         return answer
#
#     def is_check(self, s2):
#         if s2[:] != s2[::-1]:
#             return False
#         return True


print(Solution.longestPalindrome(' ', 'cbbd'))