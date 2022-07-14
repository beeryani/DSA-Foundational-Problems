'''
General Theme Sliding Window technique
Note: Picking problems from this resource:
https://medium.com/techie-delight/top-problems-on-sliding-window-technique-8e63f1e2b1fa
Morning Session:
Problem no 1:  : Done; had to change approach in terms from Kadane to Sliding Window
Problem no 2: https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/ : Done; had to look really closely at HIGHEST and LOWEST of K scores :/

Evening Session:
Problem no 3: https://leetcode.com/problems/minimum-size-subarray-sum/ : Naive Approach worked: Prefix Sum Approach is time efficient but not space efficient as a large input size can take
up large memory spaces.

Problem no 4: https://leetcode.com/problems/contains-duplicate-ii/ : Naive Approach worked : Wrong Answer in a particular test case
'''

#example problem to establish pattern

'''
Types of sliding windows:
1. Statically Sized Sliding Window: Problem 1
2. Dynamically Sized Sliding Window
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


'''
Problem 2
Minimum Difference between k numbers randomly picked
'''

# iteration 1 based on the above principle of dynamic sliding window technique

def minimumDifference(nums, k):
    nums.sort()
    start, end = 0, k - 1;
    minDiff = currDiff = 1e8;

    while end < len(nums):
        currDiff = nums[end] - nums[start];
        minDiff = min(minDiff, currDiff);
        start += 1;
        end += 1;

    return minDiff

# print(f"{minimumDifference([9, 4, 1, 7, 8],4)}")

'''
Problem 3:
Minimum Size Subarray Sum

#Iteration 1: Prefix Sum based solution
def minSubArrayLen(target, nums):
    #calculating the prefixSum array of the input array
    def prefixSum(nums):
        tempSum = nums[0]
        for i in range(1, len(nums)):
            tempSum += nums[i]
            nums[i] = tempSum
        return nums
    
    start, end = 0, len(nums) - 1
    nums = prefixSum(nums) # calling helper function

    while (end < len(nums)):
        if ((nums[end] - nums[start]) > target):
            start += 1;
        elif ((nums[end] - nums[start] == target)):
            return end - start
    return 0

print(f"{minSubArrayLen(7, [2,3,1,2,4,3])}")
'''

#iteration 2; Dyanmic Sliding Window Technique being applied:

def minSubArrayLen(target, nums):
    #calculating the prefixSum array of the input array
    n = len(nums);
    maxLength = n + 1;
    windowSum, start, currentLength = 0, 0, maxLength;

    for end in range(len(nums)):
        windowSum += nums[end]
        while (target <= windowSum):
            currentLength = min(currentLength, end - start + 1);
            windowSum -= nums[start];
            start += 1;

    return currentLength if currentLength != maxLength else 0


print(f"{minSubArrayLen(7, [2,3,1,2,4,3])}")

'''
Problem No 4:
Subarray Product less than K:
'''

# iteration no 1: dynamic sliding window to save on space complexity

def numSubarrayProductLessThanK(nums, k):
    resultCount = 0;
    for end in range(len(nums)):
        start = end;
        product = 1;
        if (nums[end] < k):
            product *= nums[start];
            resultCount += 1;
            end += 1;
        
        while (end < len(nums)):
            if (product < k):
                product *= nums[end];
                end += 1;
                resultCount += 1;
            else:
                break

    return resultCount - 1 if resultCount != 0 else 0;

print(f"{numSubarrayProductLessThanK([10,5,2,6], 100)}")