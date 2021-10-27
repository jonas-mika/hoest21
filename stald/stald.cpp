#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::vector;

int max(vector<int> vec) {
    int max_ = vec[0];
    for (int i=1; i<vec.size(); i++) {
        if (vec[i] > max_) {
            max_ = vec[i];
        }
    }
    return max_;
}

int min(vector<int> vec) {
    int min_ = vec[0];
    for (int i=1; i<vec.size(); i++) {
        if (vec[i] < min_) {
            min_ = vec[i];
        }
    }
    return min_;
}

int main() {
    string s;
    int count;
    vector<int> counts; 

    counts.push_back(0);
    while (getline(cin, s) && !s.empty()) {
        if (s == "Får ind") {
            count++;
        } else if (s == "Får ud") {
            count--;
        }
        counts.push_back(count);
    }

    cout << max(counts) - min(counts) << endl;

    return 0;
}
