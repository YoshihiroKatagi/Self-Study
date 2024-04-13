#include <iostream>
#include <vector>
#include <queue>
using namespace std;

const int INF = 1<<29;

int main() {
    int K;
    cin >> K;

    vector<int> dist(K, INF);
    deque<int> que;

    dist[1] = 1;
    que.push_front(1);

    while (!que.empty()) {
        int v = que.front();
        que.pop_front();

        int v2 = (v * 10) % K;
        if (dist[v2] > dist[v]) {
            dist[v2] = dist[v];
            que.push_front(v2);
        }

        v2 = (v + 1) % K;
        if (dist[v2] > dist[v] + 1) {
            dist[v2] = dist[v] + 1;
            que.push_back(v2);
        }
    }

    cout << dist[0] << endl;
}