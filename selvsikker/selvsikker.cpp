#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::vector;
using std::transform;

string replace_all(string s, string old, string new_) {
    while (s.find(old) != string::npos) {
        s.replace(s.find(old), s.size(), new_);
    }

    return s;
}

string lower(string s) {
    /*
    transform (s.begin(), s.end(), s.begin(), tolower);

    return s;
    */
    for (int i=0; i<s.length();i++) {
        cout << s[i] << endl;
        s[i] = tolower(s[i]);
    }

    return s;
}

string capitalise(string s) {
    transform (s.begin(), s.begin()+1, s.begin(),  toupper);
    transform (s.begin()+1, s.end(),   s.begin()+1, tolower);

    return s;
    /*
    for (int i=0; i<s.length();i++) {
        if (i == 0) {
            s[i] = toupper(s[i]);
        } else {
            s[i] = tolower(s[i]);
        }
    }
    return s;
    */
}

// helper function for parsing string according to delimiter 
vector<string> split (string s, string delimiter) {
    size_t pos_start = 0, pos_end, delim_len = delimiter.length();
    string token;
    vector<string> res;

    while ((pos_end = s.find (delimiter, pos_start)) != string::npos) {
        token = s.substr (pos_start, pos_end - pos_start);
        pos_start = pos_end + delim_len;
        res.push_back (token);
    }

    res.push_back (s.substr (pos_start));
    return res;
}

vector<string> swap(vector<string> s) {
    string temp = s[0];
    s[0] = capitalise(s[1]);
    s[1] = lower(temp);
     
    return s;
}

int main() {
    setlocale(LC_ALL, "da-DK");

    string s;
    string delimiter = " ";

    getline(cin, s);
    s = replace_all(s, "?", "!");

    vector<string> words = split(s, delimiter);
    words = swap(words);  

    for (int i=0; i<words.size(); i++) {
        if (i == words.size() - 1) {
            cout << words[i] << endl;
        } else {
            cout << words[i] << " ";
        }
    }

    return 0;
}
