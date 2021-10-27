#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    for (int i=1; i<=n;i++) {
        if (i % 3 == 0 && i % 5 == 0) {
            cout << "øfgrynt" << endl;
        } else if (i % 3 == 0) {
            cout << "øf" << endl;
        } else if (i % 5 == 0) {
            cout << "grynt" << endl;
        } else {
            cout << i % 100 << endl;
        }
    }

    return 0;
}
