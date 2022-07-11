'''
# general theme on two pointer problems
Problem no 1: https://leetcode.com/problems/merge-sorted-array/
Problem no 2: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

'''
'''
Applying two pointer approach:

for i in range(m):
    

'''


'''
Problem 2 of the day: Two Sum II
'''

'''
Solution Iteration 1:
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0;
        end = len(numbers) - 1 
        currSum = 0 # too much memory space required to reach here.
    
        while (end > start):
            currSum = numbers[start] + numbers[end]

            if (currSum > target):
                end -= 1;
            if (currSum == target):
                return [start + 1, end + 1]

            if (end == start):
                end = len(numbers) - 1;
                start += 1;
        return "no result";

'''
def twoSum(numbers, target):
    start = 0;
    end = len(numbers) - 1
    
    while (end > start):
        if (numbers[start] + numbers[end] > target):
            end -= 1;
        elif (numbers[start] + numbers[end] == target):
            return [start + 1, end + 1]
        else:
            start += 1;
            
    


print(twoSum([2,7,11,15],9))