// Competitive Programming 3
// Problem 11565

#include <iostream>
#include <cmath>
using namespace std;

// A = x + y + z
// B = xyz
// C = x^2 + y^2 + z^2

int main(){
    int T, A, B, C, x, y, z;
    cin >> T;

    while (T--){
        bool found = false;
        cin >> A >> B >> C;
        int xcap = (int) sqrt(C) + 1;

        for (x = -xcap; x < xcap; x++){
            int ycap = (int) sqrt(C-x*x) + 1;
            for (y = -ycap; y < ycap; y++){
                z = A - x - y;
                if (x == y || x == z || y == z) continue;
                if (x*y*z == B){
                    if (x*x + y*y + z*z == C){
                        found = true;
                        printf("%d %d %d\n", x, y, z);
                        break;
                    }
                }
            }
            if (found) break;
        }
        if (!found) printf("No solution.\n");
    }
    return 0;
}
