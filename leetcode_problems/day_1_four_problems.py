'''
# general theme on two pointer problems
Problem no 1: https://leetcode.com/problems/merge-sorted-array/ : Not Yet
Problem no 2: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/ : Done
Problem no 3: https://leetcode.com/problems/valid-palindrome/ : Done
Problem no 4: https://leetcode.com/problems/remove-duplicates-from-sorted-array/ : One Solution proposed

Evening Set:
Problem no 5: https://leetcode.com/tag/two-pointers/: https://leetcode.com/problems/remove-element/ : Done using referring a solution, in line with the iterative approach
Problem no 6: https://leetcode.com/problems/move-zeroes/ : Naive Solution Processed
'''
'''
Problem 1 of the day: Merge Sorted Array    
'''
def merge(nums1, nums2, m, n):
    pointerOne, pointerTwo = 0, 0




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

'''
Problem 3 of the day: Valid Palindrome
Optimal Solution in one iteration
'''

import re

def isPalindrome(s):
    s = re.sub('[^A-Za-z0-9]+', '', s)
    s = s.lower()

    if (len(s) == 0):
        return True
    
    start, end = 0, len(s) - 1;

    while (end > start):
        if (s[start] == s[end]):
            end -= 1;
            start += 1;
        elif (s[start] != s[end]):
            return False
        
    return True


s = "kayak"

print(f"{isPalindrome(s)}")

'''
Problem 4 of the day: Remove Duplicates from the Sorted Array
Solution Iteration No 1:
def removeDuplicates(nums):
    start, end = 0, len(nums) - 1
    k = 0

    while (end > start):
        if (nums[start] == nums[end]):
            del nums[end];
            nums.append("_");
            start += 1;
            k += 1;
            end = len(nums) - 1
        elif(nums[start] != nums[end]):
            end -= 1;
    
    return nums, k

Solution two:
def removeDuplicates(nums):
    start = 0
    k = 0

    while (start < len(nums) - 1):
        end = len(nums) - 1;
        while (start < end):
            if (nums[end] == nums[start]):
                del nums[end];
                nums.append("_");
                end -= 1;
                k += 1;
            else:
                end -= 1;
        start += 1;
        
        return nums, k
nums = [0,0,1,1,1,2,2,3,3,4]
'''


def removeDuplicates(nums):
    start, end = 0, len(nums) - 1
    k = 0

    while (end > start):
        if (nums[start] == nums[end]):
            del nums[end];
            nums.append("_");
            start += 1;
            end = len(nums) - 1
        elif(nums[start] != nums[end]):
            end -= 1;
            k += 1;
    
    return k


nums = [0,0,1,1,1,2,2,3,3,4]
print(f"{removeDuplicates(nums)}")


'''
Problem No 5:
Remove Element

First Solution:
def removeElement(nums, val):
    start = 0;
    k = 0;
    while (start < len(nums)):
        if (nums[start] == val):
            del nums[start]
            nums.append("_")
            start += 1;
            print(start)
        else:
            start += 1;
            k += 1
    
    return k, nums

print(f"{removeElement([0,1,2,2,3,0,4,2], 2)}")
'''

def removeElement(nums, val):
    k = 0;
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1;
    return k

print(f"{removeElement([0,1,2,2,3,0,4,2], 2)}")


'''
Problem No 6:
Move Zeroes
'''

def moveZeroes(nums):
    start = 0;
    end = 1;
    while(end < len(nums)):
        if ((nums[start] == nums[end])):
            end += 1;
        elif ((nums[start] == 0)):
            nums[start], nums[end] = nums[end], nums[start]
            start += 1;
            end += 1;
    return nums
    
print(f"{moveZeroes([1,0])}")




