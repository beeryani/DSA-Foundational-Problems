'''
Sorting Algorithms
Bubble Sort -> Swapping each element in case of arr[j] > arr[j + 1]
Example code to learn sorting algorithms for Data Structure and Algorithms preparation 
https://www.geeksforgeeks.org/bubble-sort/ 

Insight based on understanding the article mentioned above
1. The operation works on dual traversal of the array
2. With each iteration of the outer loop, we reduce the size of the list by 1
Why? because the algorithm optimises to place the largest element of the sequence at the very end of the array.
It is an in-place algorithm as it doesn't create any major change to the shape of the data structure.
'''

### general implementation of bubble sort
def bubbleSort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if (arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

testArray = [90, 30, 45, 23, 56, 66, 92, 99] ## input array

resultArray = bubbleSort(testArray)

print(f"This is the input array {testArray}, and this is the output array {resultArray}")

### optimisation to the above approach
'''
In case of no swap, the inner loop can be breaked and the next iter can be initiated.
The array runs n^2 times, by introducing the swapFlag, we can remove the inner lop iterations that don't lead to a swap
'''

def optimisedBubbleSort(arr, N):

    for i in range(N-1):
        swapFlag = False
        for j in range(N - i - 1):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapFlag = True

        if(swapFlag == False):
                break
    return arr

testArray = [90, 30, 45, 23, 56, 91, 92, 99] ## input array

resultArray = optimisedBubbleSort(testArray, len(testArray))

print(f"This is the input array {testArray}, and this is the output array {resultArray}")



