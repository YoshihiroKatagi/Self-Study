#include <iostream>
#include <vector>
int main() {
    using namespace std;
    unsigned N;
    cin >> N;
    vector<unsigned> B(N, N); // B[i] := 人 i の直後の人（いなければ N）
    unsigned front;
    for(unsigned i = 0; i < N; ++i){
        int A;
        cin >> A;
        --A; // 0-indexed に直しておく
        if(A < 0)
            front = i;
        else
            B[A] = i; // 人 i の直前が人 A ⇔ 人 A の直後が人 i
    }
    while(front < N){ // N になるまで（= 直後の人がいなくなるまで）直後に移動を繰り返す
        cout << front + 1 << " ";
        front = B[front];
    }
    cout << endl;
    return 0;
}