// Competitive Programming 3
// Problem 616

#include <iostream>
#include <cmath>
using namespace std;

int main(){
    while (1){
        int N;
        cin >> N;
        if (N < 0) break;

        bool works = false;
        int p;

        for (p = (int)(sqrt(N)+0.5); p > 1; p--){
            works = true;
            int n = N;

            for (int q = 0; q < p; q++){
                int take = n / p;
                int rem = n % p;

                if (rem != 1){
                    works = false;
                    break;
                }
                else
                    n -= take + 1;
            }

            if (n % p != 0)
                works = false;

            if (works) break;
        }

        printf("%d coconuts, ", N);
        if (!works) printf("no solution\n");
        else printf("%d people and 1 monkey\n", p);
    }
    return 0;
}
