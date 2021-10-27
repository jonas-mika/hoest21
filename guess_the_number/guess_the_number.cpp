#include <iostream>

using std::cin;
using std::cout;
using std::string;
using std::endl;

int main() {
    int guess = 500;
    int min = 1;
    int max = 1000;
    string response;

    cout << guess << endl;
    cin >> response;


    while (response != "correct") {
        
        if (response == "lower") {
            max = guess - 1;
            guess = min + (max - min) / 2;
        } else if (response == "higher") {
            min = guess + 1;
            guess = min + (max - min) / 2;
        }

        // cout << "min: " << min << " " << "max: " << max << endl;
        cout << guess << endl;

        cin >> response;
    }
}
