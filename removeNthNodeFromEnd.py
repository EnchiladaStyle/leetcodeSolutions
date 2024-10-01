# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        
        dummyNode = ListNode(next=head)
        leftPointer = dummyNode
        rightPointer = head

        while rightPointer != None:
            if n > 0:
                n -= 1
            else:
                leftPointer = leftPointer.next
            rightPointer = rightPointer.next
        leftPointer.next = leftPointer.next.next
        return dummyNode.next