// Competitive Programming 3
// Problem 11340

#include <cstdio>
#include <iostream>
#include <string>
#include <map>
using namespace std;

int main(){
    int T;
    cin >> T;

    while(T--){
        int K;
        scanf("%d", &K);
        map <char, double> values;

        while(K--){
            char character;
            int val;
            scanf(" %c %d", &character, &val);
            values[character] = val;
        }

        int count = 0;
        string line;
        line.reserve(10005);
        scanf("%d", &K);
        getline(cin, line); // newline

        while (K--){
            getline(cin, line);
            for (char c : line){
                if (values.find(c) != values.end()){
                    count += values[(int)c];
                }
            }
        }

        printf("%d.%.2d$\n", count/100, count%100);
    }








    return 0;
}
