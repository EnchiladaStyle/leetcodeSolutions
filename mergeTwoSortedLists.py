# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        
        list1Pointer = list1
        list2Pointer = list2
        head = None
        current = None

        if list1 == None:
            return list2
        if list2 == None:
            return list1

        if list1Pointer.val < list2Pointer.val:
            head = list1Pointer
            list1Pointer = list1Pointer.next
        else:
            head = list2Pointer
            list2Pointer = list2Pointer.next
        current = head

        while list1Pointer != None and list2Pointer != None:
            if list1Pointer.val < list2Pointer.val:
                current.next = list1Pointer
                list1Pointer = list1Pointer.next
            else:
                current.next = list2Pointer
                list2Pointer = list2Pointer.next
            current = current.next
        
        if list1Pointer == None and list2Pointer == None:
            return head
        if list1Pointer == None:
            current.next = list2Pointer
        else:
            current.next = list1Pointer
        return head