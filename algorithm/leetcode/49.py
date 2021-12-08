import collections
from typing import List

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         dict1 = collections.defaultdict(list)
#         for str in strs:
#             dict1[''.join(sorted(str))].append(str)
#
#         return dict1.values()


# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         dict1 = {}
#         for str in strs:
#             tmp = ''.join(sorted(str))
#             if tmp not in dict1:
#                 dict1[tmp] = []
#
#             dict1[tmp].append(str)
#
#         answer = []
#         for key in dict1.keys():
#             answer.append(dict1.get(key))
#         return answer


# my code
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = collections.defaultdict(list)
        for str in strs:
            counter[''.join(sorted(str))].append(str)

        answer = []
        for key in counter.keys():
            answer.append(counter.get(key))
        return answer


print(Solution.groupAnagrams('',["eat","tea","tan","ate","nat","bat"]))