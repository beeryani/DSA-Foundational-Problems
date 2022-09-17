'''
Two Sample Problems from the Educative Course
Problem 1: Implement Division by 2 Method
'''
from lib2to3.pytree import convert
from math import remainder
from stack import Stack;

def SolutionOne(input_number):
    s = Stack()
    answer = ""
    
    while input_number != 0:
        remainder = input_number % 2;
        s.push(remainder);
        input_number = int(input_number / 2)
    
    for item in range(s.getLength()):
        answer += str(s.pop())
        
    return answer

print(SolutionOne(2432))