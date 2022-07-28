# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        dummyHead = ListNode(0, head)
        pre, curr = None, head
        
        while curr != None:
            if pre != None and pre.val == curr.val:
                pre.next = curr.next
                curr = curr.next
            else:
                pre, curr = curr, curr.next
        return dummyHead.next
        