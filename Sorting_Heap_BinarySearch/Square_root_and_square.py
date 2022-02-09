#Find x such that x^2 + sqrt(x) = C with the precision at least 6 digits after the point

#Input:
#  The sole line of the input contains one double 1.0 <= C <= 10^10

#Output:
#  The sole like of the output should contain the required x


from math import sqrt
from math import log2

EPS = 1e-10

def g(x, C):
  return x*x + sqrt(x) - C

if __name__ == "__main__":
  C = float(input())
  left, right = sqrt(C) / 2, C
  h = int(log2((right - left) / EPS))
  for i in range(h):
    middle = (right + left) / 2
    if g(middle, C) < 0:
      left = middle
    elif g(middle, C) > 0:
      right = middle
  print((right + left) / 2)
