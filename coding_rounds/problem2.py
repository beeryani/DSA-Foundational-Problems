'''
Given an array of size N, find continuous subarray with maximum number of elements whose sum is divisible by 7.

Input:
First line has an integer N, size of given array.
Next N lines have integers denoting elements of array.
Constraints
1   ≤   N   ≤   50,000
0   ≤   Each element ≤   106

Output:
Single integer, denoting maximum number of elements in required subarray.

Problem Hypothesis: Use hash table   to store probable cases
'''
length = input()
count = 0;
array = []
while (count < int(length)):
     s = input()
     if s:
         array.append(int(s))
         count += 1
     else:
        break

def solution(array, length):
    if (length != 0):
        start = 0;
        end = len(array);
        while start < int(length) and start < end:
            if (sum(array[start: end]) % 3 != 0):
                start += 1;
                if (sum(array[start: end]) % 3 != 0):
                    end -= 1;
                else:
                    return len(array[start: end]);
            else:
                return len(array[start: end]);
        return 0
    else:
        return 0
print(solution(array, length))
    

