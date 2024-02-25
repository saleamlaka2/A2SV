# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next:
            return head
        elif left==right:
            return head
        else:
            temp=head
            temp2=None
            for _ in range(left):
                temp2=temp
                temp=temp.next
            # print(temp.val,temp2.val)
            dummy=temp2
            temp3=head
            temp4=None
            for _ in range(left-1):
                temp4=temp3
                temp3=temp3.next
            # print(temp4.val)
            k=right-left
            cur=None
            while k:
                cur=temp
                temp=temp.next
                cur.next=temp2
                temp2=cur
                k-=1
            # print(cur.val,temp.val,temp2.val)
            if temp4:
                temp4.next=cur
            # else:
            #     return cur
            dummy.next=temp
            if left==1:
                head=cur
            return head

        
            