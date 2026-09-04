class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
        self.length = 0
    
    def get(self, index: int) -> int:
        i = 0
        currentNode = self.head.next # account for dummy node
        while i < index and currentNode:
            currentNode = currentNode.next
            i+=1 
        return currentNode.val if currentNode else -1

    def insertHead(self, val: int) -> None:
        insert = ListNode(val)
        insert.next = self.head.next # set new equal to head
        self.head.next = insert
        # account for empty list: tail is new node and so is head
        if not insert.next: 
            self.tail = insert
        

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val) # add after current tail
        self.tail = self.tail.next # new tail point to new node

    def remove(self, index: int) -> bool:
        i = 0
        currentNode = self.head
        while currentNode and i < index:
            currentNode = currentNode.next
            i += 1  # ends at index

        if currentNode and currentNode.next: # if node and next node exists, index is allowed
            if currentNode.next == self.tail:  
                # if the next node is the end, set the tail to the current node instead
                self.tail = currentNode
            # if next next has a value it becomes that (moves backward)
            # if we're at the tail it just becomes None
            currentNode.next = currentNode.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        arr = []
        currentNode = self.head.next # account for dummy node
        while currentNode:
            arr.append(currentNode.val)
            currentNode = currentNode.next
        return arr

