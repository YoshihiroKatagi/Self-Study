#include <iostream>
#include <vector>
using namespace std;

int main() {
    long int N;
    cin >> N;
    
    long int ans = 0;
    for (long int i = 1; i*i*i <= N; i++) {
        long int K = i*i*i;
        string K_str = to_string(K);

        int flag = 1;
        int K_len = K_str.length();
        // cout << "i: " << i << endl;
        // cout << "K_len: " << K_len << endl;
        // cout << "K: " << K << endl;
        // cout << endl;
        for (int j = 0; j < K_len/2; j++) {
            if (K_str[j] != K_str[K_len - 1 - j]) {
                // cout << "K_str[j]: " << K_str[j] << ", K_str[K_len - 1 - j]: " << K_str[K_len - 1 - j] << endl;
                flag = 0;
                break;
            }
        }
        if (flag == 1) {
            ans = K;
        }
    }
    cout << ans << endl;
}