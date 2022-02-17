# You have to implement the data structure that supports the following operations:
# 1. 1 x - add x to an end of the data structure
# 2. 2 - retrieve the last element from the data structure
# 3. 3 -  find the minimal element in the data structure

# Input:
#  The first line of the input contains one integer n (1 <= n <= 10^6) - the number of operations.
#  Next n lines contain the description of operations, one per line. The argument x in an operation
#  of the first type lies in [-10^9, 10^9]. It is guaranteed that before retrieval the data structures
#  is not empty.

# Output:
#  Output the result for each operation of the third type, one per line.

# Example:
#  Input:
#   8
#   1 2
#   1 3
#   1 -3
#   3
#   2
#   3
#   2
#   3

#  Ouput:
#  -3
#   2
#   2



class Stack(object):
  def __init__(self):
    self.array = []
    self.min = []

  def push(self, x):
    self.array.append(x)
    self.min.append(min(x, self.min[-1]) if self.min else x)
  
  def pop(self):
    self.array.pop()
    self.min.pop()

  def minimum(self):
    return self.min[-1]


if __name__ == "__main__":
  stack = Stack()
  n = int(input())
  for i in range(n):
    command = input().split()
    if command[0] == '1':
      stack.push(int(command[1]))
    elif command[0] == '2':
      stack.pop()
    else:
      print(stack.minimum())
