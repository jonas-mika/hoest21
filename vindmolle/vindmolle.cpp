#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int absolute(int x) {
    if (x < 0) {
        return -x;
    } else {
        return x;
    }
}

int main() {
    int b, a;
    int with_clock, against_clock;

    cin >> b >> a;

    with_clock = 360 - b;
    against_clock = - b;


    if (a > b) {
        with_clock -= 360 - a;
        against_clock -= 360 - a;
    }  else {
        with_clock += a;
        against_clock += a;
    }

    if (with_clock < absolute(against_clock)) {
        cout << with_clock << endl;
    } else if (with_clock > absolute(against_clock)) {
        cout << against_clock << endl;
    } else {
        cout << 180 << endl;
    }

    return 0;
}
