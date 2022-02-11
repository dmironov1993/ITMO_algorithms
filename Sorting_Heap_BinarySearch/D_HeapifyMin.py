#This is similar to D_HeapifyMaxpy that can be found here 
#https://github.com/dmironov1993/ITMO_algorithms/blob/main/Sorting_Heap_BinarySearch/D_HeapifyMax.py
#but this time we construct the heap so that minimum element could be extracted by O(log(n))

def insert(x, length):
  a.append(x)
  i = length
  while i > 0 and a[i] < a[(i-1)//2]:
    a[i], a[(i-1)//2] = a[(i-1)//2], a[i]
    i = (i-1)//2

def remove_min(a, length):
  a[0], a[length-1] = a[length-1], a[0]
  res = a.pop()
  i = 0
  while True:
    j = i
    if 2*i + 1 < length-1 and a[2*i + 1] < a[j]:
      j = 2*i + 1
    if 2*i + 2 < length - 1 and a[2*i + 2] < a[j]:
      j = 2*i + 2
    if i == j:
      break
    a[i], a[j] = a[j], a[i]
    i = j
  return res
