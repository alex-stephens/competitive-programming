// Competitive Programming 3
// Problem 11517

#include <iostream>
#include <cstring>
using namespace std;

#define INF (1<<30)

int main(){
    int T;
    cin >> T;

    while (T--){
        int V, n, i;
        cin >> V;
        cin >> n;

        int notes[n];
        for (i = 0; i < n; i++)
            cin >> notes[i];

        int total = V + 10001;
        int dp[total];
        for (int i = 0; i < total; i++) dp[i] = INF;
        dp[0] = 0;

        for (int n : notes){
            for (int i = total - n + 1; i >= 0; i--){
                if (dp[i] != INF)
                    dp[i+n] = min(dp[i+n], dp[i] + 1);
            }
        }

        i = V;
        while (dp[i] == INF)
            i++;
        printf("%d %d\n", i, dp[i]);
    }
    return 0;
}
