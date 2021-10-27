#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int n;
    cin >> n;
    int prev_x, x, prev_y, y;
    int res1, res2;
    int min_x, min_y, z;
    prev_x = prev_y = 25;
    x = y = 50;

    cout << "?" << " " << prev_x << " " << y << endl << flush;
    cin >> res1;

    cout << "?" << " " << x << " " << y << endl << flush;
    cin >> res2;

    min_x = (res2 - res1 + pow(prev_x, 2) - pow(x, 2)) / (2 * prev_x - 2 * x);

    cout << "?" << " " << x << " " << prev_y << endl << flush;
    cin >> res1;

    cout << "?" << " " << x << " " << y << endl << flush;
    cin >> res2;

    min_y = (res2 - res1 + pow(prev_y,2) - pow(y, 2)) / (2 * prev_y - 2 * y);

    cout << "?" << " " << min_x << " " << min_y << endl << flush;
    cin >> z;
    z = sqrt(z);

    cout << "!" << " " << min_x << " " << min_y << " " << z << endl << flush;

    return 0;
}
