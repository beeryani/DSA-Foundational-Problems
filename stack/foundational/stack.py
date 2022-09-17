'''
Stack: https://www.educative.io/courses/ds-and-algorithms-in-python/YMBEM0VZN2p
'''
'''
In this chapter we will implement stack DS in Python and see every step of the process.
'''
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

#initialise Stack
exampleStack = Stack()
#input items in the stack
exampleStack.push(2)
#second item added
exampleStack.push(3)
#third element added
exampleStack.push(4)
#pop function
exampleStack.pop()
#returns final stack
print(exampleStack.getStack())
#checks whether the stack is empty or not
print(exampleStack.IsStackEmpty())
#returns the top element on the stack
print(exampleStack.peek())
