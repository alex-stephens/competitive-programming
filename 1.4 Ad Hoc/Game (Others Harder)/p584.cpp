// Competitive Programming 3
// Problem 584

#include <iostream>
#include <cstring>
#include <algorithm>
#include <string>
#include <cctype>
using namespace std;

int main() {
    char c;
    int frameBonus[12];

    while (1){
        int score = 0, f = 0, rollsDone = 1;
        cin >> c;
        if (c == 'E') break;

        memset(frameBonus, 0, 12*sizeof(frameBonus[0]));

        while (f < 12){

            if (isdigit(c)){
                score += (c - '0') * frameBonus[f];
                rollsDone++;
            }
            else if (c == '/'){
                score += 10 * frameBonus[f];
                if (f <= 10) frameBonus[f+1] += 1;
                rollsDone = 2;
            }
            else if (c == 'X'){
                score += 10 * frameBonus[f];
                if (f <= 10){
                    frameBonus[f+1] += 1;
                    frameBonus[f+2] += 1;
                }
                rollsDone = 2;
            }

            if (rollsDone == 2){
                f++;
                rollsDone = 0;
            }

        }
        cout << score << endl;

    }




    return 0;
}
