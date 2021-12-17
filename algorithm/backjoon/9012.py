import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s = list(input().strip())
    s_dict = {')': '('}
    stack = []
    for char in s:
        if char not in s_dict:
            stack.append(char)
        elif not stack:
            print('NO')
            break
        else:
            stack.pop()
    else:
        if stack:
            print('NO')
        else:
            print('YES')

# import sys
# input = sys.stdin.readline
#
# n= int(input())
# while n > 0:
#     s = input().strip()
#     s_dict = {')': '('}
#     stack = []
#     flag = False
#     for x in s:
#         if x not in s_dict:
#             stack.append(x)
#         elif not stack or stack.pop() != s_dict[x]:
#             flag = True
#
#     if flag or len(stack) > 0:
#         print('NO')
#     else:
#         print('YES')
#
#     n -= 1