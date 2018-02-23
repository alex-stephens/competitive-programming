// Competitive Programming 3
// Problem 10784

#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

#define SIZE 80
long dp[SIZE];

long ways(int n){
    if (dp[n] != 0) return dp[n];
    return dp[n] = ways(n-2) + ways(n-3);
}

int main(){
    int n;
    memset(dp, 0, SIZE*sizeof(dp[0]));
    dp[0] = 1; dp[1] = 1; dp[2] = 2;
    while (cin >> n){
        cout << ways(n) << endl;
    }
    return 0;
}
