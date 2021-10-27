#include <iostream>

using namespace std;

int main() {
    double s, m, ans;
    bool e = false;
    int n;
    cin >> n;

    for (int i=0; i<n; i++) {
        int w;
        cin >> w;

        if (e == true) {
            e = false;
            continue;
        }

        if (w < 10 || w > 2000) {
            e = true;
            continue;
        }
        s += w;
        m += 1;
    }
    ans = s / m;
    cout << ans << endl;
    return 0;
}
