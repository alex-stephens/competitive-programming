// Competitive Programming 3
// Problem 11955

#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

int catalan[] = {1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796};

int main(){
    int N, i = 0;
    while(cin >> N){
        if (i++ > 0) cout << endl;
        cout << catalan[N] << endl;
    }
    return 0;
}
