# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        curr = result
        
        up = False
        while l1 or l2 or up:
            l1Number = l1.val if l1 else 0
            l2Number = l2.val if l2 else 0
            upNumber = 1 if up else 0

            newValue = (l1Number + l2Number + upNumber) % 10
            up = True if (l1Number + l2Number + upNumber) > 10 else False

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            next = ListNode(newValue)
            curr.next = next
            curr = next
        return result.next



