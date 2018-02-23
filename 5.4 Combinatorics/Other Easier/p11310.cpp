// Competitive Programming 3
// Problem 11310

#include <iostream>
#include <cstring>
using namespace std;

#define SIZE 50
unsigned long long dp[SIZE];

unsigned long long ways(int n){
    if (dp[n] > 0) return dp[n];
    else return dp[n] = 2*ways(n-3) + 4*ways(n-2) + ways(n-1);
}

int main(){
    int T;
    cin >> T;
    memset(dp, 0, SIZE*sizeof(dp[0]));
    dp[0] = 1, dp[1] = 1, dp[2] = 5;    // base cases

    while (T--){
        int n;
        cin >> n;
        cout << ways(n) << endl;
    }
    return 0;
}
