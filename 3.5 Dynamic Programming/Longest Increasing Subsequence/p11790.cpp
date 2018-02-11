// Competitive Programming 3
// Problem 11790

#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int T;
    cin >> T;
    int height[10000], width[10000], inc[10000], dec[10000];

    for (int t = 1; t < T+1; t++){
        int N;
        cin >> N;
        for (int i = 0; i < N; i++){
            cin >> height[i];
        }
        for (int i = 0; i < N; i++){
            cin >> width[i];
            inc[i] = width[i], dec[i] = width[i];
        }

        for (int i = 0; i < N; i++){
            for (int j = 0; j < i; j++){
                if (height[i] > height[j] && inc[i] < inc[j] + width[i]){
                    inc[i] = inc[j] + width[i];
                }
                if (height[i] < height[j] && dec[i] < dec[j] + width[i]){
                    dec[i] = dec[j] + width[i];
                }
            }
        }

        int maxInc = *max_element(inc , inc + N);
        int maxDec = *max_element(dec , dec + N);

        printf("Case %d. ", t);
        if (maxInc >= maxDec){
            printf("Increasing (%d). Decreasing (%d).\n", maxInc, maxDec);
        }
        else{
            printf("Decreasing (%d). Increasing (%d).\n", maxDec, maxInc);
        }
    }
    return 0;
}
