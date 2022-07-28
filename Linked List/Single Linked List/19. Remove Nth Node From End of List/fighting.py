# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        dummyNode1, dummyNode2 = ListNode(0, head), ListNode(0, head)
        pre = dummyNode1
        for i in range(n):
            dummyNode2 = dummyNode2.next
            
        while dummyNode2 and dummyNode2.next:
            pre = pre.next
            dummyNode2 = dummyNode2.next
        
        pre.next = pre.next.next
        return dummyNode1.next