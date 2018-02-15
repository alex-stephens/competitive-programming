// Competitive Programming 3
// Problem 10306

#include <iostream>
#include <cstring>
using namespace std;

const int INF = 1 << 30;

int main(){
    int N, m, S;
    cin >> N;

    while (N--){
        cin >> m >> S;
        int c1[m], c2[m];
        for (int i = 0; i < m; i++){
            cin >> c1[i] >> c2[i];
        }
        int A[S+1][S+1];
        for (int i = 0; i < S+1; i++){
            for (int j = 0; j < S+1; j++){
                A[i][j] = INF;
            }
        }
        A[0][0] = 0;

        for (int i = 0; i < S+1; i++){
            for (int j = 0; j < S+1; j++){
                for (int c = 0; c < m; c++){
                    if (i >= c1[c] && j >= c2[c])
                        A[i][j] = min(A[i][j], A[i-c1[c]][j-c2[c]] + 1);
                }
            }
        }
        int minCoins = INF;
        for (int i = 0; i < S+1; i++){
            for (int j = 0; j < S+1; j++){
                if (i*i + j*j == S*S){
                    minCoins = min(minCoins, A[i][j]);
                }
            }
        }

        if (minCoins >= INF)
            cout << "not possible" << endl;
        else
            cout << minCoins << endl;
    }




    return 0;
}
