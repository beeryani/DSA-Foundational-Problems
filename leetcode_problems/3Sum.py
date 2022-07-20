def Solution(nums):
    res = []
    nums.sort()
    for i, a in enumerate(nums):
        if i >0 and a == nums[i - 1]:
            continue
        else:
            start, end = i + 1, len(nums) - 1

            while end > start:
                threeSum = a + nums[end] + nums[start]

                if threeSum > 0:
                    end -= 1;
                elif threeSum < 0:
                    start += 1;
                elif threeSum == 0:
                    res.append([a, nums[start], nums[end]])
                    start += 1;
                    while nums[start] == nums[start - 1] and start < end:
                        start += 1  
    
    return res

                

    
    
    

print(Solution([-3, 3, 4, -3, 1, 2]))