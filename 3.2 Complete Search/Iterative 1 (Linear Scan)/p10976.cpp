// Competitive Programming 3
// Problem 927

#include <iostream>
using namespace std;

int main() {
    int k;

    while (cin >> k){
        int solX[10000], solY[10000];
        int x, y = k + 1;
        int N = 0;

        while ((float)1/k - (float)1/y <= (float)1/(k+1)){
            if ((k * y) % (y - k) == 0){
                x = (k * y) / (y - k);

                if (x < y)
                    break;

                solX[N] = x;
                solY[N] = y;
                N += 1;
            }
            y += 1;
        }

        cout << N << endl;
        for (int i = 0; i < N; i++)
            printf("1/%d = 1/%d + 1/%d\n", k, solX[i], solY[i]);
    }
    return 0;
}
