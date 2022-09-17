def targetIndices(nums, target):
    start, end = 0, len(nums) - 1
    answer_left, answer_right = -1, -1
    answer = []
    nums.sort()
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

    if answer_left == answer_right:
        answer.append(answer_left)
    else:
        for idx in range(answer_left, answer_right + 1):
            answer.append(idx)
            
    return answer
    
print(targetIndices([1, 2, 5, 2, 3], 2))