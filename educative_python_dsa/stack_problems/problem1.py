'''
Sample Problem No 1 in Stacks on Educative

Declare the Stack properly; the error that came in this runtime was due to lack of return statement in the method "pop" being called
'''
from stack import Stack

def Solution(inputString):
    s = Stack();
    flag = True;
    start = 0;

    def matchingFunction(elem1, elem2):
        if elem1 == '[' and elem2 == ']':
            return True
        elif elem1 == '{' and elem2 == '}':
            return True
        elif elem1 == '(' and elem2 == ')':
            return True
        else:
            return False
 
    while start < len(inputString) and flag:
        stackElement = inputString[start];
        if stackElement in "({[":
            s.push(stackElement)
        else:
            if s.IsStackEmpty():
                flag = False;
                break
            else:
                topElement = s.pop();
                if matchingFunction(topElement, stackElement) != True:
                    flag = False;
                    break;
        start += 1;
    
    if s.IsStackEmpty() and flag:
        return True
    else:
        return False

testString = "{[]"
print(Solution(testString))

print(type("5"))
