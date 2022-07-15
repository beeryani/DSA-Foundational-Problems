'''
https://leetcode.com/problems/subarray-sum-equals-k/
'''

def Solution(arr, k):
    currSum = 0
    start, end = 0, 0
    for i in range(len(arr)):
        if(currSum < k):
            currSum += arr[i]
            end = i + 1
    
    for j in range(len(arr)):
        if (currSum > k):
            currSum -= arr[j]
            start = j + 1
    
    print(start + 1, end)
    return currSum

nums = [1,2,3,4,5,6,7,8,9,10]

print(f"{Solution(nums, 15)}")