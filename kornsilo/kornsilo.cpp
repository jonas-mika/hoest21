#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main() {
    int n, k, h;
    int ans;

    cin >> n >> k >> h;

    ans = n / h  - k;

    if (n%h != 0) {
        ans += 1;
    }

    if (ans < 0) {
        ans = 0;
    }

    cout << ans << endl;

    return 0;
}
