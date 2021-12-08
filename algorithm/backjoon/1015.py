import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
answer = [-1] * n
for i in range(n):
    idx = arr.index(min(arr))
    answer[idx] = i
    arr[idx] = 1001

print(*answer)