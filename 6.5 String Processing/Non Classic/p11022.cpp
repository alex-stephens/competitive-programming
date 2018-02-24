// Competitive Programming 3
// Problem 11022

#include <iostream>
#include <cstring>
#include <string>
using namespace std;

#define SIZE 85
int memo[SIZE][SIZE];
string str;

int longest(int i, int j){
    // base cases (length 1 and 2)
    if (memo[i][j] > 0) return memo[i][j];
    if (i == j) return memo[i][j] = 1;
    if (i == j - 1){
        if (str[i] == str[j]) return memo[i][j] = 1;
        else return memo[i][j] = 2;
    }

}

int main(){
    while (cin >> str){
        if (str[0] == '*') break;
        memset(memo, 0, SIZE*SIZE*sizeof(memo[0][0]));

    }
    return 0;
}
