# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            if prev and curr.val == val:
                prev.next = curr.next
                curr = curr.next
                continue
            elif not prev and curr.val == val:
                curr = curr.next
                head = head.next
                continue
            prev = curr
            curr = curr.next
        return head
            


        