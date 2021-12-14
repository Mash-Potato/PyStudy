# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1) or (list2 and list1.val > list2.val):
            list1 ,list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1


# class linknode:
#     def __init__(self, val=0, next=None):
#         self.val=val
#         self.next=next
#
# class Solution:
#     def mergetwolist(self, list1:Optional[linknode], list2:Optional[linknode]) -> Optional[linknode]:
#         arr = []
#         while list1 is not None:
#             arr.append(list1.val)
#             list1 = list1.next
#
#         while list2 is not None:
#             arr.append(list2.val)
#             list2 = list2.next
#
#         arr.sort()
#
#         print(arr)
