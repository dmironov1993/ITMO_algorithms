//You are given two arrays. The first one is sorted, while the second one contains queries in form of integer numbers.
//For each query you need to output a number from the first array so that the number is the closest to the number from a query.
//If there are several such numbers, you need to output minimum among them.

//Input:
// In the first line there are numbers n and k (0 < n, k <= 10^5). 
// In the second line there are n numbers related to the first array that is sorted.
// In the third line there are k numbers related to the second array.
// Absolute value of each number in both arrays is smaller than 2 * 10^9.

//Output:
// For each of k numbers you need to output a number from the first array that is as close to the input value as possible.
// The answer to each query must be on a separate line.

//Example:
// Input:
//  5 5
//  1 3 5 7 9
//  2 4 8 1 6

// Output:
//  1
//  3
//  7
//  1
//  5


#include <iostream>

int binSmaller(int a[], int n, int number) {
  int left = -1;
  int right = n;
  while (right - left > 1) {
    int middle = left + (right - left) / 2;
    if (a[middle] < number) {
      left = middle;
    } else {
      right = middle;
    }
  }
  if (right == n)
    return n - 1;
  return right;
}

int binBigger(int a[], int n, int number) {
  int left = -1;
  int right = n;
  while (right - left > 1) {
    int middle = left + (right - left) / 2;
    if (a[middle] <= number) {
      left = middle;
    } else {
      right = middle;
    }
  }
  if (left == -1)
    return 0;
  return left;
}

int main()
{
  int n, k;
  std::cin >> n >> k;
  int a[n];
  int tmp;
  for (auto i = 0; i < n; i++) {
    std::cin >> tmp;
    a[i] = tmp;
  }
  for (auto i = 0; i < k; i++) {
    std::cin >> tmp;
    int left = binSmaller(a, n, tmp);
    int right = binBigger(a, n, tmp);
    int num1 = a[left];
    int num2 = a[right];
    int dist1 = std::abs(tmp - num1);
    int dist2 = std::abs(tmp - num2);
    if (dist1 < dist2)
      std::cout << num1 << '\n';
    else if (dist1 > dist2)
      std::cout << num2 << '\n';
    else
      std::cout << std::min(num1, num2) << '\n';
  }
  return 0;
}
