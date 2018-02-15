// Competitive Programming 3
// Problem 10855

#include <iostream>
using namespace std;

int main(){
    while (1){
        int N, n;
        char c;
        cin >> N >> n;
        if (N == 0 && n == 0) break;

        int big[N][N], small[n][n];
        for (int i = 0; i < N; i++){
            for (int j = 0; j < N; j++){
                cin >> c;
                big[i][j] = (int) c;
            }
        }
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                cin >> c;
                small[i][j] = (int) c;
            }
        }

        int count[] = {0,0,0,0};

        // correct orientation
        for (int i = 0; i < N-n+1; i++){
            for (int j = 0; j < N-n+1; j++){
                bool match = true;
                for (int x = 0; x < n; x++){
                    for (int y = 0; y < n; y++){
                        if (big[i+x][j+y] != small[x][y]){
                            match = false;
                            break;
                        }
                    }
                    if (!match) break;
                }
                if (match) count[0] += 1;
            }
        }

        // rotated 90 degrees
        for (int i = 0; i < N-n+1; i++){
            for (int j = 0; j < N-n+1; j++){
                bool match = true;
                for (int x = 0; x < n; x++){
                    for (int y = 0; y < n; y++){
                        if (big[i+x][j+y] != small[n-1-y][x]){
                            match = false;
                            break;
                        }
                    }
                    if (!match) break;
                }
                if (match) count[1] += 1;
            }
        }

        // rotated 180 degrees
        for (int i = 0; i < N-n+1; i++){
            for (int j = 0; j < N-n+1; j++){
                bool match = true;
                for (int x = 0; x < n; x++){
                    for (int y = 0; y < n; y++){
                        if (big[i+x][j+y] != small[n-1-x][n-1-y]){
                            match = false;
                            break;
                        }
                    }
                    if (!match) break;
                }
                if (match) count[2] += 1;
            }
        }

        // rotated 270 degrees
        for (int i = 0; i < N-n+1; i++){
            for (int j = 0; j < N-n+1; j++){
                bool match = true;
                for (int x = 0; x < n; x++){
                    for (int y = 0; y < n; y++){
                        if (big[i+x][j+y] != small[y][n-1-x]){
                            match = false;
                            break;
                        }
                    }
                    if (!match) break;
                }
                if (match) count[3] += 1;
            }
        }

        cout << count[0] << ' ' << count[1] << ' ';
        cout << count[2] << ' ' << count[3] << endl;


    }
    return 0;
}
