#You are given an array of integers. Your task is to sort them in non-decreasing order.
#Input:
#  The first line of the input contains one integer n (1 ≤ n ≤ 100000) — the number of elements in the array. 
#  The second line contains n integers which do not exceed 10^9 by absolute value.

#Output:
#  The sole line of the output should contain the same array but in the non-decreasing order. 
#  The elements should be separated by space.

#Example:
#Input:
  10
  1 8 2 1 4 7 3 2 3 6
#Output:
  1 1 2 2 3 3 4 6 7 8 
  
  

def mergeSort(array, length):
  if length > 1:
    middle = length // 2
    L = array[:middle]
    R = array[middle:]
    mergeSort(L, middle)
    mergeSort(R, length - middle)
    i, j, k = 0, 0, 0
    while i < middle and j < length - middle:
      if L[i] < R[j]:
        array[k] = L[i]
        i += 1
        k += 1
      else:
        array[k] = R[j]
        j += 1
        k += 1
    while i < middle:
      array[k] = L[i]
      i += 1
      k += 1
    while j < length - middle:
      array[k] = R[j]
      j += 1
      k += 1

if __name__ == "__main__":
  n = int(input())
  array = [*map(int, input().split())]
  mergeSort(array, n)
  print(*array)
