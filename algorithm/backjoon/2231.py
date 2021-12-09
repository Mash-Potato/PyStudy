import sys

n = input()
tmp = int(n) - 9 * len(n)
if tmp < 1:
    tmp = 1

for i in range(tmp, int(n)):
    sum1 = i + sum(map(int, str(i)))

    if sum1 == int(n):
        print(i)
        sys.exit(0)

print(0)