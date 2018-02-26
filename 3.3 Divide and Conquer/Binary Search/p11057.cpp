// Competitive Programming 3
// Problem 11057

#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
    int N, n, M, diff, start;
    vector<int> v;
    vector<int>::iterator it;

    while (cin >> N){
        v.clear();
        for (int i = 0; i < N; i++){
            cin >> n;
            v.push_back(n);
        }

        sort(v.begin(), v.end());
        diff = *(--v.end());

        cin >> M;

        for (int x : v){
            it = lower_bound(v.begin(), v.end(), M - x);
            int y = *it;
            if (it != v.end() && x + y == M){

                // only allow x=y if the number appears twice
                if (abs(x-y) < diff && (abs(x-y) != 0 || y == *(it+1))){
                    diff = abs(x-y);
                    start = min(x,y);
                }
            }
        }

        printf("Peter should buy books whose prices are %d and %d.\n\n", start, start+diff);
    }
    return 0;
}
