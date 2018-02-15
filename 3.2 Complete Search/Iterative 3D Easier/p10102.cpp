// Competitive Programming 3
// Problem 10102

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int M;
    while (cin >> M){

        int grid[M][M];

        char c;
        for (int i = 0; i < M; i++){
            for (int j = 0; j < M; j++){
                cin >> c;
                grid[i][j] = (int) c - '0';
            }
        }

        int maxMinDist = 0;

        for (int i = 0; i < M; i++){
            for (int j = 0; j < M; j++){
                //cout << grid[i][j] << endl;
                if (grid[i][j] != 1)
                    continue;

                int minDist = 2*M - 2;

                for (int x = 0; x < M; x++){
                    for (int y = 0; y < M; y++){
                        if (grid[x][y] != 3)
                            continue;

                        minDist = min(minDist, abs(x-i) + abs(y-j));
                    }
                }
                maxMinDist = max(maxMinDist, minDist);
            }
        }
        cout << maxMinDist << endl;
    }
    return 0;
}
