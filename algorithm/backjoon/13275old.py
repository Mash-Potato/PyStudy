import sys

s = input()

# 예외 처리
if s == s[::-1]:
    print(len(s))
    sys.exit(0)

# 팰린드롬 판별 ,확장
i = l = 0
for j in range(len(s)):
    if s[j-l:j+1] == s[j-l:j+1][::-1]:
        i, l = j-l, l+1
    elif j-l > 0 and s[j-l-1:j+1] == s[j-l-1:j+1][::-1]:
        i, l = j-l-1, l+2

print(l)