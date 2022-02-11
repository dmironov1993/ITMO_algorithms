#In this problem, you have to implement a data structure that supports two operations:

#insert(x) — add an integer x;
#extract — extract the maximal element.

#Input
#The first line of the input contains one integer n (1 ≤ n ≤ 100 000) — the number of performed operations.

#Next n lines contain operations, one per line. The operations of the first type have a format "0 x" where 1 ≤ x ≤ 107. 
#The operations of the second type have a format "1".

#It is guaranteed that before any operation of the second kind the structure is not empty.

#Output
#The output should contain the results of extract operations in the corresponding order.

#Example:
#Input:
#  7
#  0 100
#  0 10
#  1
#  0 5
#  0 30
#  0 50
#  1

#Output:
#  100
#  50


def insert(x, a, length):
  a.append(x)
  #length += 1
  i = length
  while i > 0 and a[i] > a[(i-1)//2]:
    a[i], a[(i-1)//2] = a[(i-1)//2], a[i]
    i = (i-1)//2

def remove_max(a, length):
  a[0], a[length-1] = a[length-1], a[0]
  res = a.pop()
  i = 0
  while True:
    j = i
    if 2*i + 1 < length-1 and a[2*i+1] > a[j]:
      j = 2*i + 1
    if 2*i + 2 < length-1 and a[2*i+2] > a[j]:
      j = 2*i + 2
    if j == i:
      break
    a[i], a[j] = a[j], a[i]
    i = j
  return res

if __name__ == "__main__":
  k = int(input())
  a = []
  n = 0
  for i in range(k):
    command = input().split()
    if command[0] == '0':
      insert(int(command[1]), a, n)
      n += 1
    elif command[0] == '1':
      print(remove_max(a, n))
      n -= 1
