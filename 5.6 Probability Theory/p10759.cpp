// Competitive Programming 3
// Problem 10759

#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

#define MAX 150
#define MAXDICE 24

// gcd of x,y where y >= x
unsigned long long gcd(unsigned long long x, unsigned long long y){
    if (x == 0) return y;
    return gcd(y%x, x);
}

int main(){
    int n, x;
    // dp[n][x] is the number of ways to get x using n dice
    unsigned long long dp[MAXDICE+1][MAX+1];
    memset(dp, 0, (MAX+1)*(MAXDICE+1) * sizeof(dp[0][0]));
    for (int x = 1; x <=6; x++) dp[1][x] = 1;

    for (int n = 2; n <= MAXDICE; n++){
        for (int x = n; x <= MAX; x++){
            for (int i = 1; i <= 6; i++){
                if (x - i > 0)
                    dp[n][x] += dp[n-1][x-i];
            }
        }
    }

    while (1){
        cin >> n >> x;
        if (n == 0 && x == 0) break;

        // answer is the sum over all values from n up to max value
        unsigned long long ways = 0;
        for (int i = x; i <= 6*n; i++) ways += dp[n][i];

        if (ways == 0){
            cout << 0 << endl;
            continue;
        }

        unsigned long long total = pow(6,n);
        if (ways == total){
            cout << 1 << endl;
            continue;
        }

        unsigned long long divisor = gcd(ways, total);
        cout << ways/divisor << "/" << total/divisor << endl;
    }
    return 0;
}
