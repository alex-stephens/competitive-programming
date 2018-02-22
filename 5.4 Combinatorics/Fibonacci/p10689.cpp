// Competitive Programming 3
// Problem 10689

#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

int main(){
    int T, a, b, M;
    unsigned long long N;
    cin >> T;
    long long period[] = {0, 60, 300, 1500, 150000};

    while (T--){
        cin >> a >> b >> N >> M;
        long long p = period[M];
        int cap = pow(10,M);
        unsigned long long Nreduced = N % p;
        long fib[] = {a, b, a+b};

        for (int n = 3; n < Nreduced + 1; n++){
            fib[n%3] = (fib[(n-1)%3] + fib[(n-2)%3]) % cap;
        }
        cout << fib[Nreduced % 3] % cap << endl;
    }

    return 0;
}
