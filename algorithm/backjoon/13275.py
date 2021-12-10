import sys

s = input()
lt = 0
answer = 0

# 예외 처리
if s == s[::-1]:
    print(len(s))
    sys.exit(0)

# 팰린드롬 판별 확장
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
    if newLen > answer:
        answer = newLen

print(answer)