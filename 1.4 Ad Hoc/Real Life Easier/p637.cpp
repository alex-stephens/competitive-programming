// Competitive Programming 3
// Problem 637

#include <iostream>
#include <cstring>
#include <algorithm>
#include <string>
using namespace std;

int main() {
    int N, sheets;
    int front[25][2], back[25][2];
    while (1) {
        cin >> N;
        if (N == 0) break;
        sheets = (N+3) / 4;
        for (int i = 0; i < sheets; i++){
            // ascending
            front[i][1] = 2*i + 1;
            back[i][0] = 2*(i+1);
            // descending - some of these numbers will be out of range
            front[i][0] = 2*sheets + 2*(sheets - i);
            back[i][1] = 2*sheets - 1 + 2*(sheets - i);
        }

        cout << "Printing order for " << N << " pages:" << endl;
        for (int i = 0; i < sheets; i++){
            // print front
            printf("Sheet %d, front: ", i+1);
            if (front[i][0] <= N) printf("%d, ", front[i][0]);
            else printf("Blank, ");
            printf("%d\n", front[i][1]);

            if (N < 2) break; // no need for back if only one side

            // print back
            printf("Sheet %d, back : ", i+1);
            if (back[i][0] <= N) printf("%d, ", back[i][0]);
            else printf("Blank, ");
            if (back[i][1] <= N) printf("%d\n", back[i][1]);
            else printf("Blank\n");
        }
    }
    return 0;
}
