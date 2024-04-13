
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int rec(a, k) {
        if (a.size() <= 100) {
            sort(a.begin(), a.end());
            return a[k];
        }

        vector<int> a2;
        for (int i = 0; i < a.size(); i += 5) {
            a2.push_back(a[i:i+5]);
        }

        int m = rec(a2, a.size()/10);

        vector<int> p, q, r;
        for (int i = 0; i < a.size(); i++) {
            if (a[i] < m) p.push_back(a[i]);
            else if (a[i] == m) q.push_back(a[i]);
            else r.push_back(a[i]);
        }

        int res;
        if (k <= p.size()) return rec(p, k);
        else if (k <= p.size() + q.size()) return m;
        else return rec(r, k - p.size() - q.size());
    }
}