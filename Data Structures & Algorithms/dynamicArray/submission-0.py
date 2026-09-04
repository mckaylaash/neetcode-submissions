class DynamicArray:
    
    def __init__(self, capacity: int):
        # 
        self.capacity = capacity
        self.DA = [0] * capacity
        self.length = 0

    def get(self, i: int) -> int:
        return self.DA[i]

    def set(self, i: int, n: int) -> None:
        self.DA[i] = n

    def pushback(self, n: int) -> None:
        # actually adding something new
        # if array is full, expand size
        # place n at next empty space
        if self.length == self.capacity:
            self.resize()
        self.DA[self.length] = n
        self.length+= 1

    def popback(self) -> int:
        # remove and return the element at the end of the array
        # temp = self.DA[self.length - 1] 
        # self.DA[self.length - 1] = 0
        # Dont forget to update length!
        self.length -= 1
        return self.DA[self.length] 

    def resize(self) -> None:
        # double the capacity
        # add self.capacity worth of empty slots then double capacity
        self.DA += [0] * self.capacity 
        self.capacity*= 2


    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
