#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N, K;
    cin >> N >> K;
    vector<int> a(N), b(N);
    for (int i = 0; i < N; i++) cin >> a[i];
    for (int i = 0; i < N; i++) cin >> b[i];

    sort(b.begin(), b.end());

    auto check = [&](long long x) -> bool {
        long long cnt = 0;
        for (int i = 0; i < N; i++) {
            cnt += upper_bound(b.begin(), b.end(), x / a[i]) - b.begin();
        }
        return (cnt >= K);
    }

    int median_num = N * (N + 1) / 4

    long long left = 0, right = 1LL<<60;
    while (right - left > 1) {
        long long mid = (left + right) / 2;
        if (check(mid)) right = mid;
        else left = mid;
    }
    cout << right << endl;
}