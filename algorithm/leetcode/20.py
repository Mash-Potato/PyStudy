import collections

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        # 스택 이용 예외 처리 및 일치 여부 판별
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0

# class Solution:
#     def isValid(self, s: str) -> bool:
#         dq: Deque = collections.deque()
#         for x in s:
#             if x == '(':
#                 dq.append(x)
#             elif x == '[':
#                 dq.append(x)
#             elif x == '{':
#                 dq.append(x)
#             elif x == ')':
#                 if not dq or dq.pop() != '(':
#                     return False
#             elif x == ']':
#                 if not dq or dq.pop() != '[':
#                     return False
#             elif x == '}':
#                 if not dq or dq.pop() != '{':
#                     return False
#         return len(dq) == 0