#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, T;
    cin >> N >> T;
    vector<int> A(T), B(T);
    for (int i = 0; i < T; i++) cin >> A[i] >> B[i];

    // vector<int> ans(T);
    vector<int> player(N, 0);
    for (int i = 0; i < T; i++) {
        player[A[i] - 1] += B[i];

        auto arranged = player;
        arranged.erase(unique(arranged.begin(), arranged.end()), arranged.end());

        // vector<int> arranged;
        // for (int value : player) {
        //     if (find(arranged.begin(), arranged.end(), value) == arranged.end()) {
        //         arranged.push_back(value);
        //     }
        // }

        // int ans_i = arranged.size();
        cout << arranged.size() << endl;
    }
}