# Merge K sorted lists (LinkedList)

# Ref: https://leetcode.com/problems/merge-k-sorted-lists/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        interval = 1
        list_len = len(lists)

        while interval < list_len:
            for idx in range(0, list_len - interval, interval * 2):
                lists[idx] = self.merge(lists[idx], lists[idx + interval])
            interval *= 2

        return lists[0]

    def merge(self, l1, l2):
        head = pointer = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                pointer.next = l1
                l1 = l1.next
                pointer = pointer.next
            else:
                pointer.next = l2
                l2 = l2.next
                pointer = pointer.next

        if l1:
            pointer.next = l1
        else:
            pointer.next = l2

        return head.next
