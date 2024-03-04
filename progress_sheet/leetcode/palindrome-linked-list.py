# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        prev=None
        cur=slow
        while cur:
            cur.next,prev,cur=prev,cur,cur.next
        l=head
        r=prev
        while r:
            if l.val!=r.val:
                return False
            r=r.next
            l=l.next
        return True


        

