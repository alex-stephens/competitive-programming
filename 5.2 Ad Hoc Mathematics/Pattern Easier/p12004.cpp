// Competitive Programming 3
// Problem 616

#include <iostream>
#include <cmath>
using namespace std;

long long triangular(long long x){
    return (x * (x+1)) / 2;
}

int main(){
    int Q, N;
    long long num;
    cin >> Q;

    for (int t = 1; t <= Q; t++){
        cin >> N;
        num = triangular(N-1);

        if (num % 2 == 0){
            printf("Case %d: %lld\n", t, num/2);
        }
        else{
            printf("Case %d: %lld/2\n", t, num);
        }
    }
    return 0;
}
