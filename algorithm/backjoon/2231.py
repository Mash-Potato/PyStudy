import sys

n = input()
start = int(n) - 9 * len(n)
if start < 1:
    start = 1

for constructor in range(start, int(n)):
    if constructor + sum(map(int, str(constructor))) == int(n):
        print(constructor)
        sys.exit(0)

print(0)