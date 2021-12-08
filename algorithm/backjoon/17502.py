n = int(input())
s = list(input())
lt = 0
rt = n-1
while lt <= rt:
    if s[lt] != s[rt]:
        if s[lt] == '?':
            s[lt] = s[rt]
        else:
            s[rt] = s[lt]
    elif s[lt] == '?':
        s[lt] = s[rt] = 'a'
    lt += 1
    rt -= 1

print(''.join(s))