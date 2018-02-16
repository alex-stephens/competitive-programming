// Competitive Programming 3
// Problem 735

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    vector <int> scores = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,
        20,21,22,24,26,27,28,30,32,33,34,36,38,39,40,42,45,48,50,51,54,57,60};
    int length = scores.size();

    int N;
    while (1){
        cin >> N;
        if (N <= 0)
            break;

        int permutations = 0, combinations = 0;

        for (int i = 0; i < length; i++){
            for (int j = 0; j < length; j++){
                int target = N - scores[i] - scores[j];
                if (!binary_search(scores.begin(), scores.end(), target))
                    continue;

                permutations += 1;
                if (scores[i] >= scores[j] && scores[j] >= target)
                    combinations += 1;
            }
        }

        if (permutations == 0)
            printf("THE SCORE OF %d CANNOT BE MADE WITH THREE DARTS.\n", N);
        else{
            printf("NUMBER OF COMBINATIONS THAT SCORES %d IS %d.\n", N, combinations);
            printf("NUMBER OF PERMUTATIONS THAT SCORES %d IS %d.\n", N, permutations);
        }
        printf("***********************************");
        printf("***********************************\n");
    }
    printf("END OF OUTPUT\n");
    return 0;
}
