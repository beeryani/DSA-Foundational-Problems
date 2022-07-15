class Stack():
    def __init__(self): # initialise your stack
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        self.items.pop();
    
    def getStack(self):
        return self.items
    
    def IsStackEmpty(self):
        return self.items == []
    
    def peek(self):
        if self.items != []:
            return self.items[-1]