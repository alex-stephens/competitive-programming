// Competitive Programming 3
// Problem 11151

#include <iostream>
#include <cstring>
#include <string>
using namespace std;

#define SIZE 1005
int memo[SIZE][SIZE];
string str;

int longest(int i, int j){
    // base cases (length 1 and 2)
    if (memo[i][j] > 0) return memo[i][j];
    if (i == j) return memo[i][j] = 1;
    if (i == j - 1){
        if (str[i] == str[j]) return memo[i][j] = 2;
        else return memo[i][j] = 1;
    }

    if (str[i] == str[j]) return memo[i][j] = longest(i+1, j-1) + 2;
    return memo[i][j] = max(longest(i+1, j), longest(i, j-1));
}

int main(){
    int T;
    cin >> T;
    getline(cin,str);   // remove rest of line from buffer

    while (T--){
        memset(memo, 0, SIZE*SIZE*sizeof(memo[0][0]));
        getline(cin,str);
        int length = str.length();

        if (length == 0){       // empty line
            cout << 0 << endl;
            continue;
        }

        cout << longest(0,length-1) << endl;
    }
    return 0;
}
