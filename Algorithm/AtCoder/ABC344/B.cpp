#include <iostream>
#include <bits/stdc++.h>
#include <cmath>
using namespace std;
int main(void){
    vector<long>v;

    while (true) {
        long a;
        cin >> a;
        v.push_back(a);
        if (a == 0) {
            break;
        }
    }
    
    int size = v.size();
    
    for(int i=size-1;i>=0;i--) {
        cout << v[i] << endl;
    }
    return 0;
}