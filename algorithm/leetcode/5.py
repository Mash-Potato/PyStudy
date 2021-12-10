class Solution:
    def longestPalindrome(self, s: str) -> str:
        lt = 0
        max_len = 0
        max_s = ''

        for rt in range(len(s)):
            if lt > 0 and s[lt - 1] == s[rt]:
                lt -= 1
            else:
                while lt < rt:
                    substr = s[lt:rt + 1]
                    if substr == substr[::-1]:
                        break
                    else:
                        lt += 1

            newLen = rt - lt + 1
            # print(s[lt:rt+1])
            if newLen > max_len:
                max_s = s[lt:rt + 1]
                max_len = newLen

        return max_len

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         # 예외 처리
#         if s == s[::-1]:
#             return s
#
#         # 팰린드롬 판별, 확장
#         i = l = 0
#         for j in range(len(s)):
#             if s[j - l:j + 1] == s[j - l:j + 1][::-1]:
#                 i = j - l
#                 l += 1
#             elif j - l > 0 and s[j - l - 1:j + 1] == s[j - l - 1:j + 1][::-1]:
#                 i = j - l - 1
#                 l += 2
#
#         return s[i:i + l]

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         # 예외 처리
#         if len(s) < 2 or s == s[::-1]:
#             return s
#
#         # 팰린드롬 판별 및 투 포인터 확장
#         def extend(lt, rt):
#             while lt >= 0 and rt <=len(s) and s[lt] == s[rt-1]:
#                 lt -= 1
#                 rt += 1
#             return s[lt +1:rt -1]
#
#         # 슬라이딩 윈도우 우측 이동
#         answer = ''
#         for i in range(len(s)):
#             answer = max(answer, extend(i, i+1), extend(i, i+2), key=len)
#         return answer

print(Solution.longestPalindrome('','babad'))