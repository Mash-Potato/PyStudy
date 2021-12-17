import collections

input()
arr = collections.Counter(input().split()).most_common()
for x in arr:
    print((x[0]+' ') * x[1], end='')