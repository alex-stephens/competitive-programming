// Competitive Programming 3
// Problem 10812

#include <iostream>
#include <cstring>
#include <algorithm>
#include <string>
using namespace std;

int main() {
    long long T, a, b, avg;
    cin >> T;

    while (T--){
        cin >> a >> b;
        if (a < b || a % 2 != b % 2)   // negative or non-integer scores
            printf("impossible\n");
        else
            printf("%lld %lld\n", (a+b)/2, (a-b)/2);
    }
    return 0;
}
