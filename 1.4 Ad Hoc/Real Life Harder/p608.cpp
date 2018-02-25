// Competitive Programming 3
// Problem 608

#include <iostream>
#include <cstring>
#include <algorithm>
#include <string>
using namespace std;

int main() {
    int T;
    string left, right, outcome;
    bool real[12], heavy[12];
    int upOrDown[12];
    cin >> T;

    while (T--){
        memset(real, 0, 12*sizeof(real[0]));            // all fake
        memset(heavy, 0, 12*sizeof(heavy[0]));          // all light
        memset(upOrDown, 0, 12*sizeof(upOrDown[0]));    // all neutral

        int maxUnbalanced = 0;

        for (int i = 0; i < 3; i++){
            cin >> left >> right >> outcome;

            // if scales are even all coins are genuine
            if (outcome == "even"){
                for (int i = 0; i < left.length(); i++){
                    real[left[i] - 'A'] = true;
                    real[right[i] - 'A'] = true;
                }
            }
            else if (outcome == "up"){
                for (int i = 0; i < left.length(); i++){
                    upOrDown[left[i] - 'A']--;
                    upOrDown[right[i] - 'A']++;

                    // if we later find coin i is fake, this tells us if it is
                    // light or heavy
                    heavy[left[i] - 'A'] = true;
                }
            }
            else {
                for (int i = 0; i < left.length(); i++){
                    upOrDown[left[i] - 'A']++;
                    upOrDown[right[i] - 'A']--;

                    // if we later find coin i is fake, this tells us if it is
                    // light or heavy
                    heavy[right[i] - 'A'] = true;
                }
            }
        }

        for (int i = 0; i < 12; i++)
            maxUnbalanced = max(maxUnbalanced, abs(upOrDown[i]));

        for (int i = 0; i < 12; i++) {
            // only one coin will be fake and have been unbalanced the max
            // amount of times IN THE SAME DIRECTION (up or down)
            if (!real[i] && abs(upOrDown[i]) == maxUnbalanced){
                printf("%c is the counterfeit coin and it is ", i+'A');
                if (heavy[i]) printf("heavy.\n");
                else printf("light.\n");
            }
        }
    }
    return 0;
}
