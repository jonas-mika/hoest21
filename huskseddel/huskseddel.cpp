#include <iostream>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::getline;
using std::swap;
using std::to_string;

void reverse_string(string& s) {
    int n = s.length();
    for (int i=0; i<n/2; i++) {
        swap(s[i], s[n-i-1]);
    }
}

int main() {
    int pw;
    cin >> pw;

    if (pw == 9999) {
        cout << "0000" << endl;
        return 0;
    }
    
    pw += 1;
    string str_pw = to_string(pw);
    
    // reversing string
    reverse_string(str_pw);

    if (str_pw.length() < 4) {
        for (int i=str_pw.length(); i<4; i++) {
            str_pw.push_back('0');
        }
    }
 
    cout << str_pw << endl;

    return 0;
}
