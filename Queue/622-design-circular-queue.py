class MyCircularQueue():
    def __init__(self, k):
        self.size = k
        self.queue = ['']*k
        self.head = -1
        self.tail = -1
        
    def enQueue(self, value):
        if not self.isFull():
            if self.head == -1:
                self.head = 0
            self.tail = (self.tail+1)%self.size
            self.queue[self.tail] = value
            return True
        else:
            return False
        
    def deQueue(self):
        if not self.isEmpty():
            if self.head ==self.tail:
                self.head,self.tail = -1,-1
            else:
                self.head = (self.head+1)%self.size
            return True
        else:
            return False

    def Front(self):
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.head]

    def Rear(self):
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.tail]

    def isEmpty(self):
        return self.head == -1 and self.tail == -1

    def isFull(self):
        return (self.tail+1)%self.size == self.head