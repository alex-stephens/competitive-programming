// Competitive Programming 3
// Problem 562

#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int T;
    cin >> T;

    while(T--){
        int N;
        cin >> N;
        int coins[N+1], total = 0;
        coins[0] = 0;
        for (int n = 1; n < N+1; n++){
            cin >> coins[n];
            total += coins[n];
        }
        int W = total/2;
        sort(coins, coins + N + 1);

        int m[N+1][W+1];
        for (int c = 0; c < N+1; c++) for (int w = 0; w < W+1; w++){
            m[c][w] = 0;
        }
        int maxValue = 0;

        for (int c = 1; c < N+1; c++){
            for (int w = 0; w < W+1; w++){
                if (coins[c] > w){
                    m[c][w] = m[c-1][w];
                }
                else {
                    m[c][w] = max(m[c-1][w], coins[c] + m[c-1][w - coins[c]]);
                }
            }
            maxValue = max(maxValue, *max_element(m[c], m[c] + W + 1));
        }

        printf("%d\n", total - 2*maxValue);
    }
    return 0;
}
