'''
Insertion Sort
https://www.geeksforgeeks.org/insertion-sort/

Suitable for Smaller Datasets

Steps to be followed in general:
1. Iterate over the array from i = 1 to i =N
2. Compare the current element to its predecessor
3. If the key element < the predecessor; compare it to the elements before, swap the greater number one position up.
'''

### general implementation

def insertionSort(arr, N):

    for i in range(1, N):
        #declaring the key element
        key = arr[i]
        #declaring the index of the predessecor element
        j = i - 1
        #comparing the key element to the predessecor element
        while (j >= 0 and key < arr[j] ):
            #swapping the elements in case key < predessecor element
            arr[j + 1] = arr[j]
            #shifting the scope of j towards left to keep on working with this process
            j -= 1
        
        arr[j + 1] = key
        print(arr[j + 1], j)

    return arr

testArray = [20, 18, 16, 13]
resultArray = insertionSort(testArray, len(testArray))

print(f"This is the input array: {testArray} and here is the output array: {resultArray}")