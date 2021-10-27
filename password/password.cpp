#include <iostream>
#include <string>
#include <vector>
using namespace std;

string res() {
    int n,k;
    string curr;
    vector<string> names;

    cin >> k >> n;
    while (getline(cin, curr)) {
        names.push_back(curr);
    }

    for (int i=1; i<names.size(); i++) {
        for (int j=i+1; j<names.size(); j++) {
            string pair = char(tolower(names[i][0])) + names[i].substr(1) 
                    + char(tolower(names[j][0])) + names[j].substr(1);
            if (pair.length() == k) {
                return pair;
            }
        }
    }
    return "*umuligt*";
}

int main() {
    cout << res() << endl;
    return 0;
}
