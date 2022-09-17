'''
problem: Mountain Array
https://leetcode.com/problems/peak-index-in-a-mountain-array/
'''
def Solution(arr):
    
    start, end = 0, len(arr) - 1

    while start < end:
        mid = (start + end)//2

        if arr[mid] > arr[mid + 1]:
            end = mid - 1
        elif arr[mid] < arr[mid + 1]:
            start = mid + 1
    
    return start, end + 1
    




arr= [3,9,8,6,4]

print(Solution(arr))