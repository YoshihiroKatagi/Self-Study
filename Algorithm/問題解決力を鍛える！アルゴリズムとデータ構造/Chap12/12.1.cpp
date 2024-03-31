#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> a(N);
    for (int i = 0; i < N; i++) cin >> a[i];

    auto b = a;
    sort(b.begin(), b.end());

    for (int i = 0; i < N; i++) {
        cout << lower_bound(b.begin(), b.end(), a[i]) - b.begin() << endl;
    }
}