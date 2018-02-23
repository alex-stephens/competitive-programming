// Competitive Programming 3
// Problem 495

#include <iostream>
#include <cstring>
using namespace std;

int main(){
    int N;
    int digits = 1050, carry, temp;
    int fib[3][digits];

    while (cin >> N){
        memset(fib, 0, sizeof(fib[0][0])*3*digits);
        fib[0][0] = 0, fib[1][0] = 1;

        for (int n = 2; n < N+1; n++){
            carry = 0;
            for (int i = 0; i < digits; i++){
                temp = fib[(n-1)%3][i] + fib[(n-2)%3][i] + carry;
                carry = temp / 10;
                fib[n%3][i] = temp % 10;
            }
        }
        printf("The Fibonacci number for %d is ", N);
        bool foundNonZero = false;
        for (int i = digits-1; i>0; i--){
            if (fib[N%3][i] != 0) foundNonZero = true;
            if (foundNonZero) cout << fib[N%3][i];
        }
        cout << endl;
    }
    return 0;
}
