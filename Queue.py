class Queue():
    def __init__(self,n):
        self.queued = [None]*n
        self.limit = n
        self.head = -1  
        # head is the index where it keep track of the items that have been removed from the stack
        self.tail = -1 
        # tails is the index that keep track of where the next item can be added
        self.avaliable = n

    def is_full(self):
        return self.tail == self.limit-1
    
    def is_empty(self):
        return self.head == -1
    
    def enqueue(self,new_item):
        if self.is_full():
            print("Its full.")
            return
        if self.is_empty():
            