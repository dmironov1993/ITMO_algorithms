// You have to implement the data structure that supports the following operations:
// 1. 1 x - add x to an end of the data structure
// 2. 2 - retrieve the last element from the data structure
// 3. 3 -  find the minimal element in the data structure

// Input:
//  The first line of the input contains one integer n (1 <= n <= 10^6) - the number of operations.
//  Next n lines contain the description of operations, one per line. The argument x in an operation
//  of the first type lies in [-10^9, 10^9]. It is guaranteed that before retrieval the data structures
//  is not empty.

// Output:
//  Output the result for each operation of the third type, one per line.

// Example:
//  Input:
//   8
//   1 2
//   1 3
//   1 -3
//   3
//   2
//   3
//   2
//   3

//  Ouput:
//  -3
//   2
//   2


#include <iostream>
#include <vector>

int main() {
  std::ios::sync_with_stdio(0);
  std::cin.tie(0);
  std::vector<int> stack;
  std::vector<int> minimum;
  int size = 0;
  int n;
  std::cin >> n;
  for (int i = 0; i < n; i++) {
    int cmd;
    std::cin >> cmd;
    int number;
    if (cmd == 1) {
      std::cin >> number;
      stack.push_back(number);
      if (size == 0)
        minimum.push_back(number);
      else
        minimum.push_back(std::min(minimum[size - 1], number));
      size++;
    } else if (cmd == 2) {
      stack.pop_back();
      minimum.pop_back();
      size--;
    } else {
      std::cout << minimum[size - 1] << "\n";
    }
  }
  return 0;
}
