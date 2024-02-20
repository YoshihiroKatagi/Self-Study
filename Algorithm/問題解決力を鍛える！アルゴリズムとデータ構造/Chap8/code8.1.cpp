#include <iostream>
#include <vector>
using namespace std;

int main() {
  vector<int> a = {4, 3, 12, 7, 11, 1, 9, 8, 14, 6};

  cout << a[0] << endl;

  cout << a[2] << endl;

  a[2] = 5;

  cout << a[2] << endl;
}