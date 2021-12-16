import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        s_cnt, stack = collections.Counter(s), []

        for char in s:
            s_cnt[char] -= 1
            if char in stack:
                continue
            # 뒤에 붙일 문자가 남아있으면 스택에서 제거
            while stack and char < stack[-1] and s_cnt[stack[-1]] > 0:
                stack.pop()
            stack.append(char)

        return ''.join(stack)


# class Solution:
#     def removeDuplicateLetters(self, s: str) -> str:
#         for char in sorted(set(s)):
#             suffix = s[s.index(char):]
#             print(set(s), set(suffix), set(s)==set(suffix))
#             if set(s) == set(suffix):
#                 return char + self.removeDuplicateLetters(suffix.replace(char, ''))
#         return ''