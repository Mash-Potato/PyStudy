import collections
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         n_dict = collections.Counter(nums)
#         heap = []
#         for key in n_dict:
#             heapq.heappush(heap, (-n_dict[key], key))
#
#         answer = []
#
#         for _ in range(k):
#             answer.append(heapq.heappop(heap)[1])
#
#         return answer