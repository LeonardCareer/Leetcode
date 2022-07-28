# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):
        dummyNode = ListNode(0, head)
        swap = None
        while head:
            if swap != None:
                head.val = swap
                swap = None
            else:
                swap = head.val
                if head.next:
                    head.val = head.next.val
            head = head.next
        return dummyNode.next