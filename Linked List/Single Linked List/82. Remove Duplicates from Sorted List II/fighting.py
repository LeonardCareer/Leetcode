# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        # pos1, pos2, pos3, if pos1 != pos2 and pos2 != pos3: pos2 must in final listNode
        dummyNode = ListNode(0, None)
        temp = dummyNode
        pre, curr = None, head
        
        while curr != None:
            nxt = curr.next
            duplicate = False
            if pre != None and pre.val == curr.val:
                duplicate = True
            
            if nxt != None and nxt.val == curr.val:
                duplicate = True
            
            if not duplicate:
                temp.next = curr
                temp = curr
            
            pre, curr = curr, curr.next
        temp.next = None
        return dummyNode.next

    def deleteDuplicates2(self, head):
        dummyNode = ListNode(0, head)

        preHead = dummyNode

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                preHead.next = head.next
            else:
                preHead = preHead.next
            
            head = head.next
        return dummyNode.next