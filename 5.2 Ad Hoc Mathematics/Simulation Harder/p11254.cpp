// Competitive Programming 3
// Problem p11254

#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int N;
    while (1){
        cin >> N;
        if (N < 0) break;
        int t, n;

        for (n = (int)sqrt(2*N) + 0.5; n > 0; n--){
            if ((2*N - n*n + n) % 2*n == 0){
                t = (2*N - n*n + n) / (2*n);
            }
            else
                continue;

            if (2*N == n*n + (2*t - 1) * n)
                break;
        }

        printf("%d = %d + ... + %d\n", N, t, t+(n-1));
    }
    return 0;
}
