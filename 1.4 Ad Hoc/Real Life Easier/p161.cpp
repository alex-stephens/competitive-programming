// Competitive Programming 3
// Problem 161

#include <iostream>
#include <cstring>
#include <algorithm>
#include <string>
using namespace std;

int main() {
    int maxTime = 5 * 60 * 60 + 1; // 5 hours
    int counts[maxTime];

    while(1) {
        memset(counts, 0, maxTime*sizeof(counts[0]));
        int x, i = 0, n = 0, start = maxTime;
        cin >> x;
        if (x == 0) break;

        do {
            start = min(start, x); // wait for one to turn off once

            // increment all time values where x is on
            for (int i = 0; i < maxTime; i++){
                if (i % (2*x) < x - 5){
                    counts[i] += 1;
                }
            }
            n++;
        } while (cin >> x && x != 0);

        bool done = false;
        for (int i = start; i < maxTime; i++){
            if (counts[i] == n){
                printf("%02d:%02d:%02d\n", i/3600, (i/60)%60, i%60);
                done = true;
                break;
            }
        }

        if (!done) printf("Signals fail to synchronise in 5 hours\n");
    }
    return 0;
}
