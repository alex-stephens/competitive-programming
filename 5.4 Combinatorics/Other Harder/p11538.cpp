// Competitive Programming 3
// Problem 11538

#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

#define SIZE 1000005
unsigned long long memo[SIZE];

unsigned long long choose2(unsigned long long x){
    if (memo[x] != 0) return memo[x];
    return memo[x] = (unsigned long long) x * (x-1);
}

int main(){
    memset(memo, 0, sizeof(memo[0])*SIZE);
    unsigned long long m, n;
    while (1){
        cin >> m >> n;
        if (m == 0 && n == 0) break;

        if (m == 1){
            cout << choose2(n) << endl;
            continue;
        }
        if (n == 1){
            cout << choose2(m) << endl;
            continue;
        }

        unsigned long long ans = 0;
        ans += m * n * (m + n - 2); // straight paths
        // diagonal paths
        for (int i = 2; i < min(m,n); i++){
            ans += 4 * choose2(i);
        }
        ans += 2*(max(m,n) - min(m,n) + 1) * choose2(min(m,n));
        cout << ans << endl;
    }
    return 0;
}
