#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

using pll = pair<long long, long long>;

int main() {
    int N;
    cin >> N;
    vector<pll> v(N);
    for (int i = 0; i < N; i++) cin >> v[i].first >> v[i].second;

    sort(v.begin(), v.end(), [&](pll a, pll b) {return a.second < b.second;});

    bool ok = true;
    long long time = 0;
    for (int i = 0; i < N; i++) {
        time += v[i].first;
        if (time > v[i].second) ok = false;
    }

    if (ok) cout << "Yes" << endl;
    else cout << "No" << endl;
}