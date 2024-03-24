#include<iostream>
#include<vector>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; i++) cin >> A[i];

    // vector<int> B(N-1);
    for (int i = 0; i < N-1; i++) {
        // B[i] = A[i] * A[i+1];
        cout << A[i] * A[i+1] << " ";
    }
    cout << endl;
}