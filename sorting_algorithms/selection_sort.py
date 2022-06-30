'''
Selection Sort:
https://www.geeksforgeeks.org/selection-sort/
It is the opposite of bubble sort from what we understand.
In Bubble sort, we optimised to place the largest number by performing swaps at the end of the array.
In Insertion sort, we tend to optimise for the smalled number by swapping it with the smallest number declared dynamically.
'''

### general implementation

def insertionSort(arr, N):
    for i in range(N):
        minIndex = i
        
        '''
        Setting the first element as the smallest,
        Running the second loop to determine the smallest
        At the end performing the swap
        '''
        for j in range(i + 1, N):
            if (arr[minIndex] > arr[j]): ### check if the minIndex is the smallest or not
                minIndex = j

        arr[minIndex], arr[i] = arr[i], arr[minIndex]

    return arr 

testArray = [90, 30, 45, 23, 56, 66, 92, 99]

resultArray = insertionSort(testArray, len(testArray))

print(f"This is the input array {testArray}, and this is the output array {resultArray}")

'''
Benefits of selection sort:
number of swaps never cross O(N), which helps in keeping the cost low when memory write is an expensive operation
the for loop is only used to identify/compare the numbers
'''