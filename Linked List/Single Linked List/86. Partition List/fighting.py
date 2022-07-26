# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head, x: int):
        dummyNode1 = less = ListNode(0)
        dummyNode2 = more = ListNode(0)
        
        while head != None:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                more.next = head
                more = more.next
                
        more.next = None
        less.next = dummyNode2.next
        return dummyNode1.next
                
        