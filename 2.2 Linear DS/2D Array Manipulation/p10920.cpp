// Competitive Programming 3
// Problem 10920

#include <iostream>
#include <cmath>
using namespace std;

int main(){
    long S, P;
    while (1){
        cin >> S >> P;
        if (S == 0 && P == 0) break;

        long N = 1;          // current position
        long n = 1;          // current ring
        while (n*n < P) n += 2;     // n is first odd value where n^2 >= P
        if (n > 1) N = (n-2) * (n-2) + 1;

        long x = (S+1)/2, y = (S+1)/2;
        if (n > 1){
            x += n/2 - 1;
            y += n/2;
        }

        // move around the current ring
        if (P != N){
            x -= min(n-2, P-N);
            N += min(n-2, P-N);
            y -= min(n-1, P-N);
            N += min(n-1, P-N);
            x += min(n-1, P-N);
            N += min(n-1, P-N);
            y += min(n-1, P-N);
            N += min(n-1, P-N);
        }
        printf("Line = %ld, column = %ld.\n", y, x);
    }
    return 0;
}
