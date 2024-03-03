#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

const double PI = acos(-1.0);

int main() {
    int A, B, C;
    cin >> A >> B >> C;

    auto func = [&](double t) -> double {
        return A * t + B * sin(C * PI * t);
    };

    double alpha = 0, beta = 200;
    for (int iter = 0; iter < 100; iter++) {
        double gamma = (alpha + beta) / 2;
        if (func(gamma) <= 100) alpha = gamma;
        else beta = gamma;
    }

    cout << fixed << setprecision(15) << alpha << endl;
}