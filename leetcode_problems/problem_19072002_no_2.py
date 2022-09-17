'''
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
Done
'''

def searchRange(nums, target):
        #first element 
        start, end = 0, len(nums) - 1
        answer_left, answer_right = -1, -1
        answer = []
        while start <= end:
            mid = (start + end)//2
            
            if target == nums[mid]:
                answer_left = mid
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
        # last element
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end)//2
        
            if target == nums[mid]:
                answer_right = mid
                start = mid + 1
            elif target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
        
        answer.append(answer_left)
        answer.append(answer_right)
        
        return answer