# In a postfix notation (Reverse Polish notation), two operands are followed by an operation. 
# For example, the sum of two numbers A and B is written as A B +. 
# The expression B C + D * means (B + C) * D, and the expression A B C + D * + means A + (B + C) * D. 
# The advantage of a postfix notation is that it does not require brackets and additional operator precedence agreements for its reading.
 
# An expression is given in the reverse Polish notation. Calculate the result.

# Input
# The input contains the expression in the postfix notation containing single-digit numbers and the operations +, -, *. 
# The string contains no more than 100 numbers and operations.

# Output
# Output the result of the expression. 
# It is guaranteed that the result of the expression, 
# as well as the results of all intermediate calculations is less than 2^31 by an absolute value.

# Example:
# Input:
# 8 9 + 1 7 - *

# Output:
# -102


if __name__ == "__main__":
  stack = []
  s = input().split()
  n = len(s)
  for i in range(n):
    if s[i].isnumeric():
      stack.append(int(s[i]))
    else:
      el2 = stack.pop()
      el1 = stack.pop()
      if s[i] == '+':
        stack.append(el1 + el2)
      elif s[i] == '-':
        stack.append(el1 - el2)
      else:
        stack.append(el1 * el2)
  print(stack[0])
