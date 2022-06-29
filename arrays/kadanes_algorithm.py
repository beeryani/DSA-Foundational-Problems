from logging import log

def maxSubArraySum(array):
    currentSum = 0
    maxSumSoFar = -1e8  ### used to define the negative minima in the first step of the opeation

    for i in range(len(array)):
        currentSum += array[i]
        if (currentSum > maxSumSoFar):
            maxSumSoFar = currentSum

        if (currentSum < 0):
            currentSum = 0
    
    return maxSumSoFar

print(maxSubArraySum([-1,-3,-4,5,5,6,6,0,-8]))
