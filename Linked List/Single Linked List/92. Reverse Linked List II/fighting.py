# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        prev, curr = dummy, head

        for i in range(left - 1):
            prev = curr
            curr = curr.next
        
        leftHead , tail= prev, curr
        
        for i in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
        
        leftHead.next = prev
        tail.next = curr

        return dummy.next