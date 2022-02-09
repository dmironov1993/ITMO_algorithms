#You are given an array of integers. Your task is to sort them in non-decreasing order again. But now use counting sort!

#Input:
#   The sole line contains the elements of the array ai separated by space (0 ≤ a_i ≤ 100).
#Output:
#   Print sorted array

#Example:
#Input:
#   7 3 4 2 5
#Output:
#   2 3 4 5 7 


def countSort(array):
  count = [0] * 101
  for el in array:
    count[el] += 1
  return count

if __name__ == "__main__":
  a = [*map(int, input().split())]
  count = countSort(a)
  ans = []
  for i in range(101):
    if count[i]:
      for j in range(count[i]):
        ans.append(i)
  print(*ans)
