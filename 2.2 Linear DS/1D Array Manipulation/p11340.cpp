// Competitive Programming 3
// Problem 11340

#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

int main() {

    string line;
    int T, K, M, count, val;
    char character;
    int values[256];

    cin >> T;
	cin.ignore();

    for (int i = 0; i < T; i++){
        fill(values, values+256, 0); // set to zeros
        count = 0;

        scanf("%d\n", &K);

        for (int j = 0; j < K; j++){
            cin >> character >> val;
            cin.ignore();

            values[(int)character] = val;
        }

        cin >> M;
        cin.ignore();

        for (int j = 0; j < M; j++){
            getline(cin, line);

            for (int k = 0; k < line.length(); k++){
                count += values[(int)line[k]];
            }
        }
        printf("%.2f$\n", (float)count/100);
    }

    return 0;
}
