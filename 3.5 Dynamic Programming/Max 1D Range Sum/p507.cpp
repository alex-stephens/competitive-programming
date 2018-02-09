// Competitive Programming 3
// Problem 10684

#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int T;
    cin >> T;

    for(int route = 1; route <= T; route++){
        int r;
        cin >> r;

        if (r <= 1){
            printf("Route %d has no nice parts\n", route);
            continue;
        }

        long long niceness[r-1];
        for (int j = 0; j < r-1; j++){
            cin >> niceness[j];
        }

        long long score[r-1];
        int length[r-1];
        for (int j = 0; j < r-1; j++){
            score[j] = 0;
            length[j] = 0;
        }

        //score[0] = max(0, niceness[0]);
        if (niceness[0] > 0){
            score[0] = niceness[0];
        }
        else{
            score[0] = 0;
        }

        if (niceness[0] >= 0){
            length[0] = 1;
        }
        else{
            length[0] = 0;
        }

        for (int i = 1; i < r-1; i++){
            //score[i] = max(score[i-1] + niceness[i], 0);
            if (score[i-1] + niceness[i] > 0){
                score[i] = score[i-1] + niceness[i];
            }
            else{
                score[i] = 0;
            }

            if (score[i] != 0){
                length[i] = length[i-1] + 1;
            }
            else {
                length[i] = 0;
            }
        }

        long long bestScore = score[0];
        int index = 0;
        for (int j = 0; j < r-1; j++){
            if (score[j] > bestScore){
                bestScore = score[j];
                index = j;
            }
        }
        int longest = length[index];
        int maxLength = 0;
        for (int i = 0; i < r-1; i++){
            if (score[i] == bestScore && length[i] > longest){
                longest = length[i];
                index = i;
            }
        }
        //printf("index = %d\n", index);
        //printf("longest = %d\n", longest);

        if (bestScore > 0){
            printf("The nicest part of route %d is between stops %d and %d\n",
                            route, index - longest + 2, index + 2);
        }
        else{
            printf("Route %d has no nice parts\n", route);
        }







    }





    return 0;


}
