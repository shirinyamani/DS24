class Queue:
    def __init__(self):
        self.items = []

    def enq(self, item):
        self.items.insert(0, item)
    
    def deq(self):
        return self.items.pop()
    
    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)