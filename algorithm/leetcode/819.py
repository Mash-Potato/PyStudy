import collections
import re
from typing import List


# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
#         print(words)
#         dict1 = collections.Counter(words)
#         print(dict1)
#         return dict1.most_common(1)[0][0]

# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
#         print(words)
#         counts = collections.defaultdict(int)
#         for word in words:
#             counts[word] += 1
#         print(counts)
#         return max(counts, key=counts.get)


# my code
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub('[^\w]', ' ', paragraph).split()
        print(paragraph)
        paragraph = [x for x in paragraph if x not in banned]
        # print(paragraph)
        dict1 = collections.Counter(paragraph)
        return dict1.most_common(1)[0][0]

print(Solution.mostCommonWord('',
"a, a, a, a, b,b,b,c, c", ["a"]))
