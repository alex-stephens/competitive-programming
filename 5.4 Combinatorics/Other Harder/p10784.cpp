// Competitive Programming 3
// Problem 10784

#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

int main(){
    int t = 0;
    while (++t){
        long long N;
        cin >> N;
        if (N == 0) break;

        // number of diagonals of an n-gon is
        // n(n-1)/2 - n = N
        // 2N = n^2 - 3n -> n^2 - 3n - 2N = 0
        // n = (3 + root(9-8N))/2

        long long n = (int) sqrt(9+8*N)/2; // this will be too small
        while (n*n - 3*n < 2*N){
            n++;
        }
        printf("Case %d: %lld\n", t, n);
    }
    return 0;
}
