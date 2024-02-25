class MyCircularQueue:

    def __init__(self, k: int):
        self.queue=[]
        self.k=k
        self.right=0
        self.left=0
    def enQueue(self, value: int) -> bool:
        if (self.right-self.left)<self.k:
            self.queue.append(value)
            self.right+=1
            return True
        else:
            return False
        

    def deQueue(self) -> bool:
        if (self.right-self.left)>0:
            self.left+=1
            return True
        else:
            return False
        

    def Front(self) -> int:
        if self.left<self.right:
            return self.queue[self.left]
        else:
            return -1

    def Rear(self) -> int:
        if self.left<self.right:
            return self.queue[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        if self.left>=self.right:
            return True
        else:
            return False
    def isFull(self) -> bool:
        if self.right-self.left>=self.k:
            return True
        else:
            return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()