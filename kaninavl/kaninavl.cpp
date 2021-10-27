#include <iostream>
using namespace std;

fib(int n) {
    if (n<=1) {
        return n;
    }
    return fib(n-1) + fib(n-2);
}

int main() {
    int n;
    cin >> n;

    for (int i=1; i<n+1; i++) {
        cout << fib(i) << endl;
    }
    return 0;
}
