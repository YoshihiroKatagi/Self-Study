#include <iostream>
#include <vector>
using namespace std;

int main() {
    int A, B;
    cin >> A >> B;
    int sum = A + B;
    for (int i = 0; i < 10; i++) {
        if (sum != i) {
            cout << i << endl;
            break;
        }
    }
}