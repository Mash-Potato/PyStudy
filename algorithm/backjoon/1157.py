import collections
import sys
input = sys.stdin.readline

list = list(input().strip().upper())

conters = collections.Counter(list)
if len(conters) > 1 and conters.most_common(1)[0][1] == conters.most_common(2)[1][1]:
    print('?')
else:
    print(conters.most_common(1)[0][0])