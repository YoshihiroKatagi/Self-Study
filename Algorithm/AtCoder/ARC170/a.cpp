#include <iostream>
#include <string>
#include <vector>
using namespace std;

template<class T> void chmin(T& a, T b) {
  if (a > b) {
    a = b;
  }
}

const int INF = 1 << 29;

int main() {
  int N;
  string S, T;
  cin >> N;
  cin >> S;
  cin >> T;

  if (T[0] == 'B' && S[0] != T[0]) {
    cout << "-1" << endl;
  } else if (T[-1] == 'A' && S[-1] != T[-1]) {
    cout << "-1" << endl;
  } else {
    int count_BtoA = 0;
    int count_AtoB = 0;

    for (int i = 0; i < N; i++) {

      if (i = 0) {

      }

    }

  //   vector<vector<int>> dp(S.size() + 1, vector<int>(T.size() + 1, INF));

  //   dp[0][0] = 0;

  //   for (int i = 0; i <= S.size(); i++) {
  //     for (int j = 0; j <= T.size(); j++) {
  //       if (i > 0 && j > 0) {
  //         if (S[i - 1] == T[j - 1]) {
  //           chmin(dp[i][j], dp[i - 1][j - 1]);
  //         }
  //         else {
  //           chmin(dp[i][j], dp[i - 1][j - 1] + 1);
  //         }
  //       }

  //       if (i > 0) chmin(dp[i][j], dp[i - 1][j] + 1);

  //       if (j > 0) chmin(dp[i][j], dp[i][j - 1] + 1);
  //     }
  //   }

  //   cout << dp[S.size()][T.size()] << endl;
  }
}