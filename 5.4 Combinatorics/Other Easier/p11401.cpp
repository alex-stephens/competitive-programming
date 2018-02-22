// Competitive Programming 3
// Problem 495

#include <iostream>
#include <cstring>
using namespace std;

int main(){
    unsigned long long N;
    while (1){
        cin >> N;
        if (N < 3) break;
        unsigned long long count = 0;
        for (unsigned long long ab = 3; ab < N; ab++){
            count += (ab-1)/2 * (N - ab);
        }
        cout << count << endl;
    }
    return 0;
}
