// Competitive Programming 3
// Problem 195

#include <iostream>
#include <cstring>
#include <algorithm>
#include <string>
using namespace std;

// return true if c1 comes strictly before c2 (strict weak ordering)
bool compare(char c1, char c2){
    char c1r, c2r; // reduced values (i.e. letter value without case)
    if (c1 >= 'a') c1r = c1 - 'a';
    else c1r = c1 - 'A';
    if (c2 >= 'a') c2r = c2 - 'a';
    else c2r = c2 - 'A';

    if (c1r < c2r) return true;             // c1 before by letter value c2
    if (c2 - c1 == 'a' - 'A') return true;  // c1 upper, c2 lower
    return false;
}

int main() {
    int T;
    cin >> T;

    while (T--){
        string str;
        cin >> str;

        sort(str.begin(), str.end(), compare); // sort using custom compare
        do {
            cout << str << endl;
        } while (next_permutation(str.begin(), str.end(), compare));
    }
    return 0;
}
