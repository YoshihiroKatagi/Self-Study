#include<bits/stdc++.h>

using namespace std;

using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, t;
    cin >> n >> t;
    vector<ll> score(n);
    map<ll, int> mp;
    mp[0] = n;
    for (int i = 0; i < t; i++) {
        int a, b;
        cin >> a >> b;
        --a;
        if (--mp[score[a]] == 0) mp.erase(score[a]);
        score[a] += b;
        ++mp[score[a]];
        cout << mp.size() << '\n';
    }
}