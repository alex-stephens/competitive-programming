// Competitive Programming 3
// Problem 11597

#include <iostream>
#include <cstring>
using namespace std;

int main(){
    int t = 0;
    while (++t){
        int n;
        cin >> n;
        if (n == 0) break;

        printf("Case %d: %d\n", t, n>>1);
    }
    return 0;
}
