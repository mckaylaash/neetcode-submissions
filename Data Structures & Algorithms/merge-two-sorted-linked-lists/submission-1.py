# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode() # initialize as empty pointing to None
        dummy = node # set equal memory location
        
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1 # move pointer node
                list1 = list1.next # move this pointer
            else:
                node.next = list2
                list2 = list2.next # move second item in list
            node = node.next
        
        # case: when one list becomes empty
        node.next = list1 or list2
        return dummy.next

        
        

