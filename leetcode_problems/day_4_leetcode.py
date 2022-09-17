'''
Day 3 was a sick day.

Day 4: Rotation towards right problem: https://leetcode.com/problems/rotate-array/ : Done
'''

def semiRotate(arr):
    for i in range(len(arr)//2):
        arr[i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[i]
    return arr

length, rotationIndex = map(int, input().split())
array = [ int(num) for num in input().split(' ') if len(num)>0 ]

rotationIndex = rotationIndex % length
array[:] = semiRotate(semiRotate(array[:rotationIndex]) + semiRotate(array[rotationIndex:]))

print(*array, sep=' ')