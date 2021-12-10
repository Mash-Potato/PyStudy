import sys
input = sys.stdin.readline

t = int(input())
while t > 0:
    n = int(input())
    answer = 0
    for i in range(1, n+1):
        answer += i * ((i+1)*(i+2)//2)
    print(answer)
    t -= 1