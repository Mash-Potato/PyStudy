class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        lt = answer = 0
        for rt, char in enumerate(s):
            # 이미 등장한 문자라면 lt 갱신
            if char in used and lt <= used[char]:
                lt = used[char] + 1
            else:
                answer = max(answer, rt - lt + 1)

            # 현재 문자의 위치 삽입
            used[char] = rt

        return answer