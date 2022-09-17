'''
Stacks
Problem 1 of the day on Stacks: https://leetcode.com/problems/baseball-game/
'''

#declare Stack Class

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

def Solution(input):
    answer = []
    lookup = [str(i) for i in range(10)]
    for i in ["+", "-", "C", "D"]:
        lookup.append(i)
    
    for j in input:
        if j == "C":
            answer.pop()
        elif j == "D":
            answer.append(answer[-1]*2)
        elif j == "+":
            answer.append(answer[-1] + answer[-2])
        else:
            answer.append(int(j))

    return sum(answer)
        
print(Solution(["5","2","C","D","+"]))
# test = ["5","2","C","D","+"]
# ans = test.pop()
# print(ans)
# print(test)