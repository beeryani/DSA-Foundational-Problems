def mergeSort(arr):
    if len(arr) > 1:

        mid = len(arr)//2

        start = arr[: mid]
        end = arr[mid: ]
        mergeSort(start);
        mergeSort(end);

        i = j = k = 0

        while i < len(start) and j < len(end):
            if (start[i] < end[j]):
                arr[k] = start[i];
                i += 1;
            else:
                arr[k] = end[j];
                j += 1
            k += 1;
        

        while i < len(start):
            arr[k] = start[i];
            i += 1;
            k += 1;
        
        while j < len(end):
            arr[k] = end[j];
            j += 1;
            k += 1;
        

if __name__ == '__main__':
    arr = [6, 65, 3, -4, 5, 10, 3, 4, 2, 21, 34]

    mergeSort(arr)

    for items in arr:
        print(items, end = " ")
    print()

            



