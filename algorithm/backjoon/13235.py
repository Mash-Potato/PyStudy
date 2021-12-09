import sys
input = sys.stdin.readline

s = input().strip()
if s != s[::-1]:
    print('false')
    sys.exit(0)

print('true')