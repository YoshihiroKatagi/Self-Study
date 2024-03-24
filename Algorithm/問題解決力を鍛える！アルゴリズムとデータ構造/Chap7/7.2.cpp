#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

using Point = pair<int,int>;

int main() {
    int N;
    cin >> N;
    vector<Point> red(N), blue(N);
    for (int i = 0; i < N; i++) cin >> red[i].first >> red[i].second;
    for (int i = 0; i < N; i++) cin >> blue[i].first >> blue[i].second;

    sort(blue.begin(), blue.end());

    vector<bool> used(N, false);

    int res = 0;
    for (int i = 0; i < N; i++) {
        int maxy = -1, maxid = -1;
        for (int j = 0; j < N; j++) {
            if (used[j]) continue;

            if (red[j].first >= blue[i].first) continue;
            if (red[j].second >= blue[i].second) continue;

            if (maxy < red[j].second) {
                maxy = red[j].second;
                maxid = j;
            }
        }

        if (maxid == -1) continue;

        ++res;
        used[maxid] = true;
    }
    cout << res << endl;
}