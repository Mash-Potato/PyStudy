import collections
import sys
input = sys.stdin.readline

dict1 = collections.Counter(input().strip())
dict2 = collections.Counter(input().strip())
print(sum((dict1-dict2).values()) + sum((dict2-dict1).values()))