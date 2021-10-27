#include <iostream>
#include <cmath>

using namespace std;

int test(int a, int b) {
    return a / b;
}

void solve() {
    int b, h;
    cin >> b >> h;
    int field[h][b];

    // load in field
    for (int y=0; y<h;y++) {
        for (int x=0; x<b;x++) {
            char c;
            cin >> c;
            if (c == '.') {
                field[y][x] = 0;
            } else {
                field[y][x] = 1;
            }
        }
    }

    // search for centers of circles
    int c_x, c_y;
    int curr, next, top;
    int center_x, center_y;
    for (int y=0; y<h;y++) {
        c_x = 0;
        for (int x=0; x<b;x++) {
            curr = field[y][x];
            if (x < b-1) {
                next = field[y][x+1]; 
            } else {
                next = -1;
            }

            if (curr == 1) {
                c_x++;
            }

            if (curr == 1 && (next == 0 || next == -1)) {
                center_x = x - floor(c_x / 2);
                c_x = 0;

                if (y > 0) {
                    top = field[y-1][center_x];
                } else {
                    top = -1;
                }

                if (top == 0 || top == -1) {
                    c_y = 0;
                    for (int j=y;j<h;j++) {
                        curr = field[j][center_x];

                        if (curr == 1) {
                            c_y++;
                        } else {
                            center_y = y + floor(c_y / 2);
                            cout << center_x << " " << center_y << endl;
                            break;
                        }
                        if (j == h-1) {
                            center_y = y + floor(c_y / 2);
                            cout << center_x << " " << center_y << endl;
                            break;
                        }
                    }
                }
            }
        }
    }
}

int main() {
    solve();

    return 0;
}
