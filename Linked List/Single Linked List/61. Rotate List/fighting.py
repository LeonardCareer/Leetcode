# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head, k: int):
        dummyNode = ListNode(0, head)
        length = 0
        
        temp = head
        while temp:
            length += 1
            temp = temp.next
        
        if length != 0:
            realK = k % length  
            
            if realK != 0:
                temp = head
                while length - realK - 1 > 0:
                    temp = temp.next
                    realK += 1

                dummyNode.next = temp.next
                temp.next = None
                newHead = dummyNode.next

                while newHead.next:
                    newHead = newHead.next
                newHead.next = head   
                
        return dummyNode.next