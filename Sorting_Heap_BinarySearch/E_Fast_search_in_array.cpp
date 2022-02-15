//You are given an array of n integers a_1, a_2, ..., a_n
//Your task is to answer on the queries of the following type: How many iterms are between l and r?

//Input:
// The first line of the input contains n - the length of the array (1 <= n <= 10^5)
// The second line contains n integers a_1, ..., a_n (-10^9 <= a_i <= 10^9)
// The third line contains integer k - number of queries (1 <= k <= 10^5)
// The following k lines contain a paor of integers (l,r) - query, described above (-10^9 <= l <= r <= 10^9)

//Output:
// The output must consist of k integers - responses for the queries

//Example: 
// Input:
//  5
//  10 1 10 3 4
//  1 10
//  2 9
//  3 4
//  2 2

// Output:
//  5 2 2 0



#include <iostream>
#include <algorithm>

int binSearch(int a[], int n, int x_min, int x_max) {
  int l, r;
  int left = -1, right = n;
  while (right - left > 1) {
    int middle = left + (right - left) / 2;
    if (a[middle] < x_min) {
      left = middle;
    } else {
      right = middle;
    }
  }
  l = right;
  left = -1, right = n;
  while (right - left > 1) {
    int middle = left + (right - left) / 2;
    if (a[middle] <= x_max) {
      left = middle;
    } else {
      right = middle;
    }
  }
  r = left;
  return r - l + 1;
}

int main()
{
  int n;
  std::cin >> n;
  int a[n];
  int tmp;
  for (auto i = 0; i < n; i++) {
    std::cin >> tmp;
    a[i] = tmp;
  }
  std::sort(a, a + n);
  int k;
  std::cin >> k;
  int x_min, x_max;
  for (auto i = 0; i < k; i++) {
    std::cin >> x_min >> x_max;
    std::cout << binSearch(a, n, x_min, x_max) << " ";
  }
  return 0;
}
