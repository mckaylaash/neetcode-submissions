# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # singly linked list 
        prev = None
        currentNode = head
        while currentNode: 
            temp = currentNode.next
            currentNode.next = prev
            prev = currentNode
            currentNode = temp
        return prev

        