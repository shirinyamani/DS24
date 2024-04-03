class Stack(object):
    def __init__(self):
        self.items = []


    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    

##########################################
stack = Stack()
print(stack.push(['Shirin']))
stack.peek()


#print(stack)
     