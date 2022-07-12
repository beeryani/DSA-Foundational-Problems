'''
General Theme Sliding Window technique
Problem no 1: https://leetcode.com/problems/maximum-average-subarray-i/ : Done; had to change approach in terms from Kadane to Sliding Window
'''

#example problem to establish pattern

'''
Types of sliding windows:
1. Statically Sized Sliding Window:
'''

#type one question

# iteration 1: LC submission: "Time exceeeded"
'''
Comments: the iteration 1 solution is based on Kadane's Algorithm; which turns out to be less efficient.

def findMaxAverage(nums, k):
    maximumAvg = -1e8;  ### used to define the negative minima in the first step of the opeation # reference from kadane's algorithms
    currentAvg = 0;

    for i in range(len(nums) - k + 1):
        currentAvg = sum(nums[i:i + k])/k
        maximumAvg = max(currentAvg, maximumAvg)
    
    return maximumAvg

print(f"{findMaxAverage([5], 1)}")
'''


    

#iteration 2: based on a small blog explanation

def findMaxAverage2(nums, k):
    maxSum = currentSum = sum(nums[: k])
    
    for i in range(k, len(nums)):
        currentSum = currentSum + nums[i] - nums[i - k]
        maxSum = max(maxSum, currentSum)
        
    return float(maxSum)/k    

print(f"{findMaxAverage2([1,12,-5,-6,50,3], 4)}")