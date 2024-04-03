class Deq(object):
    def __init__(self):
        self.items = []

    def addrear(self, item):
        self.insert(0,item)


    def addfront(self, item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        self.items.pop(0)

    def isEmpty(self):
        return self.items == []
    
    def size(self):
        self.len(self.items)

