#include <iostream>
using namespace std;


int main() {
    int n;
    cin >> n;

    unsigned long long int f1 = 0;
    unsigned long long int f2 = 1;
    unsigned long long int fib;
    
    cout << f2 << endl;
    for (int i=2; i<n+1; i++) {
        fib = f1 + f2;
        cout << fib << endl;
        f1 = f2;
        f2 = fib;
    }
    return 0;
}
