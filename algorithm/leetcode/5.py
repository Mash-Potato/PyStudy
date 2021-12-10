class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 예외 처리
        if len(s) < 2 or s == s[::-1]:
            return s

        # 팰린드롬 판별 및 투 포인터 확장
        def extend(lt, rt):
            while lt >= 0 and rt <=len(s) and s[lt] == s[rt-1]:
                lt -= 1
                rt += 1
            return s[lt +1:rt -1]

        # 슬라이딩 윈도우 우측 이동
        answer = ''
        for i in range(len(s)):
            answer = max(answer, extend(i, i+1), extend(i, i+2), key=len)
        return answer