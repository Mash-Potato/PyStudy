import collections
import sys
input = sys.stdin.readline

arr = list(input().strip().upper())
cntdict = collections.Counter(arr)

if len(cntdict) > 1 and cntdict.most_common(1)[0][1] == cntdict.most_common(2)[1][1]:
    print('?')
else:
    print(cntdict.most_common(1)[0][0])