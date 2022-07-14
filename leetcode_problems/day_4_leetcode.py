'''
Day 3 was a sick day.

Day 4: Rotation towards right problem: https://leetcode.com/problems/rotate-array/ : Done
'''

nums = [1,2,3,4,5,6,7]
k = 3

def semiRotate(arr):
    for i in range(len(arr)//2):
        arr[i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[i]
    return arr
k = k % len(nums) # important step
nums[:] = semiRotate(semiRotate(nums[:len(nums) - k]) + semiRotate(nums[len(nums) - k:])) #important steps

