# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k: int):
        dummyNode = ListNode(0, head)
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        
        if length != 0:
            times = length // k
            
            newHead, pre, curr = dummyNode, None, head
            
            for i in range(times):
                pre = None
                for j in range(k):
                    temp = curr.next
                    curr.next = pre
                    pre, curr = curr, temp
                temp2 = newHead.next
                newHead.next = pre
                newHead = temp2
                newHead.next = curr
        
        return dummyNode.next
        