class DynamicArray:
    
    def __init__(self, capacity: int): 
        assert capacity > 0
        self.capacity = capacity
        self.size = 0
        self.l = [None] * self.capacity


    def get(self, i: int) -> int:
        assert 0 <= i < self.size 
        return self.l[i]

    def set(self, i: int, n: int) -> None:
        assert 0 <= i < self.size
        self.l[i] = n


    def pushback(self, n: int) -> None:
        if(self.size == self.capacity):
            self.resize()
        self.l[self.size] = n
        self.size += 1


    def popback(self) -> int:
        back = self.l[self.size - 1]
        self.l[self.size - 1] = None
        self.size -= 1
        return back
 

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_l = [None] * new_capacity
        for i in range(self.size):
            new_l[i] = self.l[i]
        self.l = new_l
        self.capacity = new_capacity    


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
