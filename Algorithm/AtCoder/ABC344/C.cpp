#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; i++) cin >> A[i];
    int M;
    cin >> M;
    vector<int> B(M);
    for (int i = 0; i < M; i++) cin >> B[i];
    int L;
    cin >> L;
    vector<int> C(L);
    for (int i = 0; i < L; i++) cin >> C[i];
    int Q;
    cin >> Q;
    vector<int> X(Q);
    for (int i = 0; i < Q; i++) cin >> X[i];
    
    sort(A.begin(), A.end());
    sort(B.begin(), B.end());
    sort(C.begin(), C.end());
    sort(X.begin(), X.end());

    // for (int q = 0; q < Q; q++) {
    //     for (int i = 0; i < N; i++) {
    //         if (A[i] > X[q]) {
    //             cout << "No" << endl;
    //             break;
    //         }

    //         for (int j = 0; j < M; j++) {
    //             if (A[i] + B[j] > X[q]) {
                    
    //                 break;
    //             }
    //         }
    //     }
    // }

    for (int q = 0; q < Q; q++) {
        int ans = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                for (int k = 0; k < L; k++) {
                    if (A[i] + B[j] + C[k] == X[q]) ans = 1;
                }
            }
        }
        if (ans == 1) cout << "Yes" << endl;
        else cout << "No" << endl;
    }

}