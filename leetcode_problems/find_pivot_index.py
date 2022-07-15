'''
https://leetcode.com/problems/find-pivot-index/
'''

def Solution(nums):
    total = sum(nums)
    leftSum = 0
    for i in range(len(nums)):
        rightSum = total - leftSum - nums[i]
        if (leftSum == rightSum):
            return i
        leftSum += rightSum


nums = [2,1,-1]

print(f"{Solution(nums)}")