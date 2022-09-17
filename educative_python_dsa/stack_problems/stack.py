class Stack():
    def __init__(self): # initialise your stack
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop();
    
    def getStack(self):
        return self.items
    
    def IsStackEmpty(self):
        return self.items == []
    
    def peek(self):
        if self.items != []:
            return self.items[-1]

    def returnStack(self):
        return print(self.items)
    
    def getLength(self):
        return len(self.items)
