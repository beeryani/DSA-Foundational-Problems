'''

'''
def rangeSum(nums, n, left, right):
    sum_new = []

    start, end = 0, n - 1
    while end < n and start < end:
        temp_sum = nums[start]
        sum_new.append(temp_sum)
        print(sum_new)
        for idx in range(start + 1, n):
            temp_sum += nums[idx]
            sum_new.append(temp_sum)
        start += 1;
    
    sum_new.sort()

    first_sum = 0
    for idx in range(len(sum_new)):
        first_sum += sum_new[idx]
        sum_new[idx] = first_sum
    print(right, sum_new, (sum_new[-1] - sum_new[0]))

    if right < len(sum_new):
        if left > 2:
            return (sum_new[right - 1] - sum_new[left - 2])
        else:
            return (sum_new[right - 1] - sum_new[0])
    else:
        if left > 2:
            return (sum_new[-1] - sum_new[left - 2])
        else:
            return (sum_new[-1] - sum_new[0])



print(rangeSum([1, 2, 3, 4], 4, 1, 10))

