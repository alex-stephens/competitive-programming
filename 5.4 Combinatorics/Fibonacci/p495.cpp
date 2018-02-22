// Competitive Programming 3
// Problem 495

#include <iostream>
using namespace std;

int main(){
    int N;
    long long fib[3];
    while (cin >> N){
        fib[0] = 0, fib[1] = 1;

        for (int n = 2; n < N+1; n++){
            fib[n%3] = fib[(n-1)%3] + fib[(n-2)%3];
        }
        printf("The Fibonacci number for %d is %lld\n", N, fib[N%3]);
    }
    return 0;
}
