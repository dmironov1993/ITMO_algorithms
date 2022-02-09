#You are given an array of integers. Your task is to sort them in non-decreasing order.
#Input:
#  The first line of the input contains one integer n (1 ≤ n ≤ 100000) — the number of elements in the array. 
#  The second line contains n integers which do not exceed 10^9 by absolute value.

#Output:
#  The sole line of the output should contain the same array but in the non-decreasing order. 
#  The elements should be separated by space.

#Example:
#Input:
#  10
#  1 8 2 1 4 7 3 2 3 6
#Output:
#  1 1 2 2 3 3 4 6 7 8 



def pivot(array, start, end):
  b = [array[start], array[start + (end - start) // 2] , array[end]]
  if b[0] > b[1]:
    b[0], b[1] = b[1], b[0]
  if b[0] > b[2]:
    b[0], b[2] = b[2], b[0]
  if b[1] > b[2]:
    b[1], b[2] = b[2], b[1]
  return b[1]

def quickSort(array, start, end):
  if (start >= end):
    return
  i, j = start, end
  p = pivot(array, start, end)
  while (i <= j):
    while (array[i] < p):
      i += 1
    while (array[j] > p):
      j -= 1;
    if (i <= j):
      array[i], array[j] = array[j], array[i]
      i += 1
      j -= 1
  quickSort(array, start, i - 1)
  quickSort(array, i, end)


if __name__ == "__main__":
  n = int(input())
  array = [*map(int, input().split())]
  quickSort(array, 0, n-1)
  print(*array)
