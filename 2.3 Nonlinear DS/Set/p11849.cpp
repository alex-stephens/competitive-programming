// Competitive Programming 3
// Problem 11849

#include <algorithm>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <string>
using namespace std;

int main(){
    while (1){
        int N, M, n, count = 0;
        cin >> N >> M;
        if (N == 0 && M == 0) break;

        set <int> s;

        while (N--){
            cin >> n;
            s.insert(n);
        }

        while (M--){
            cin >> n;
            if (s.find(n) != s.end()) count++;
        }

        cout << count << endl;
    }
    return 0;
}

// Alternate implementation using map instead of set - theoretically faster
// but actually slower on UVa
/*
int main(){
    while (1){
        int N, M, n, count = 0;
        cin >> N >> M;
        if (N == 0 && M == 0) break;

        map <int, int> s;

        while (N--){
            cin >> n;
            s[n] = 1;
        }

        while (M--){
            cin >> n;
            if (s[n] == 1) count++;
        }

        cout << count << endl;
        s.clear();
    }
    return 0;
}
*/
