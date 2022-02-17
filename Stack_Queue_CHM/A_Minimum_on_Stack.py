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
