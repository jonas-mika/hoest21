#include <iostream>
#include <iomanip>

using namespace std;

double shoelace(double x[], double y[], int n) {
    double area = 0.0;

    // Calculate value of shoelace formula
    int j = n - 1;
    for (int i = 0; i < n; i++) {
        area += (x[j] + x[i]) * (y[j] - y[i]);
        j = i;  // j is previous vertex to i
    }
    return abs(area / 2.0);
}

int main() {
    int n;
    double ans;
    cin >> n;
    double x[n];
    double y[n];

    for (int i=0;i<n;i++) {
        cin >> x[i] >> y[i];
    }

    ans = shoelace(x, y, n);
    cout << fixed << setprecision(1) << ans << endl;

    return 0;
}
