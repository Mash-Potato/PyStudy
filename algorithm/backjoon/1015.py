n = int(input())
a = list(map(int, input().split()))
b = sorted(a)
p = []
for i in range(n):
    p.append(b.index(a[i]))
    b[p[i]] = 1001

for x in p:
    print(x, end=' ')

print(*p)

# import sys
# input = sys.stdin.readline
#
# n = int(input())
# arr = list(map(int, input().split()))
# answer = [-1] * n
# for i in range(n):
#     idx = arr.index(min(arr))
#     answer[idx] = i
#     arr[idx] = 1001
#
# print(*answer)