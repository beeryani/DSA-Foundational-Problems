'''
Binary Search
'''
def binarySearch(arr, element):
    start, end = 0, len(arr) - 1
    answer = -1
    while end >= start:
        mid = (end + start)//2
        print(f"This is our middle element : {mid}")
        
        if element < arr[mid]:
            end = mid - 1
        elif element > arr[mid]:
            start = mid + 1
        elif element == arr[mid]:
            answer = mid
            start = mid + 1
    
    return answer
    

print(binarySearch([1, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5], 5))

'''
Random Array; [1, 2, 4, 5, 5, 6, 6, 6, 7, 10, 2, 3]
Number of pair
'''

def Solution(arr):
    count = 0
    for left in range(len(arr)):
        for right in range(left + 1, len(arr)):
            if arr[left] == arr[right]:
                count += 1
    
    return count

print(Solution([1, 2, 4, 5, 6, 5, 6, 6, 6, 7, 10, 2, 3]))


def optimatSolution(arr):
    dictionaryOne = {}
    for idx in range(len(arr)):
        ele = arr[idx]
        if ele in dictionaryOne:
            dictionaryOne[ele] += 1
        else:
            dictionaryOne[ele] = 1
    
    answer = 0
    for k, v in dictionaryOne.items():
        if v > 1:
            answer += (v*(v - 1))//2
    return answer

print(optimatSolution([1, 2, 4, 5, 6, 5, 6, 6, 6, 7, 10, 2, 3]))

