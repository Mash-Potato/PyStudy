import collections
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        # 홀수일때
        if fast:
            slow = slow.next
        
        # 팰린드롬 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         q: Deque = collections.deque()
#         if not head:
#             return True
#
#         node = head
#         while node is not None:
#             q.append(node.val)
#             node = node.next
#
#         while len(q) > 1:
#             if q.popleft() != q.pop():
#                 return False
#
#         return True

# my code
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         arr = []
#
#         while head is not None:
#             arr.append(head.val)
#             head = head.next
#
#         if arr == list(reversed(arr)):
#             return True
#         else:
#             return False


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         q: List = []
#
#         if not head:
#             return True
#
#         node = head
#         while node is not None:
#             q.append(node.val)
#             node = node.next
#
#         while len(q) > 1:
#             if q.pop(0) != q.pop():
#                 return False
#
#         return True