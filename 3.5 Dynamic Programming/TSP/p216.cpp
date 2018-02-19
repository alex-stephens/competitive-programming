// Competitive Programming 3
// Problem 357

#include <iostream>
#include <cstring>
using namespace std;

int main(){

    int N;
    int coins[] = {0, 1, 5, 10, 25, 50};
    int C = 5;
    while (cin >> N){
        long ways[C+1][N+1];
        memset(ways, 0, sizeof(ways[0][0]) * (C+1) * (N+1));

        for (int n = 0; n < N+1; n++)
            ways[1][n] = 1;
        for (int c = 0; c < C+1; c++)
            ways[c][0] = 1;

        for (int c = 2; c < C+1; c++){
            for (int n = 1; n < N+1; n++){
                ways[c][n] = ways[c-1][n];
                if (n >= coins[c])
                    ways[c][n] += ways[c][n - coins[c]];
            }
        }
        long num = ways[C][N];
        if (num <= 1)
            printf("There is only 1 way to produce %d cents change.\n", N);
        else
            printf("There are %ld ways to produce %d cents change.\n", num, N);
    }
    return 0;
}
