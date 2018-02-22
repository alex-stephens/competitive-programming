// Competitive Programming 3
// Problem 11955

#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

long long memo[55][55];

long long choose(int n, int k){
    if (memo[n][k] != 0) return memo[n][k];
    if (k == 0 || n == k) return memo[n][k] = 1;
    else return memo[n][k] = choose(n-1, k-1) + choose(n-1, k);
}

int main(){
    memset(memo, 0, sizeof(memo[0][0])*55*55);
    int T;
    cin >> T;

    for (int t = 1; t < T+1; t++){
        char a[105], b[105], s[10], c;
        memset(a, 0, 105*sizeof(a[0]));
        memset(b, 0, 105*sizeof(b[0]));
        int N;
        while (cin >> c) if (c == '(') break;
        int i = 0;
        cin >> c;
        while (c != '+'){
            a[i++] = c;
            cin >> c;
        }
        cin >> c;
        i = 0;
        while (c != ')'){
            b[i++] = c;
            cin >> c;
        }
        while (cin >> c) if (c == '^') break;
        cin >> N;

        cout << "Case " << t << ": ";

        for (int i = 0; i < N+1; i++){
            long long coeff;

            // a printing
            if (N - i > 0){
                coeff = choose(N, i);
                if (coeff > 1) cout << coeff << "*";
                cout << a;
                if (N-i > 1) cout << "^" << N-i;
            }

            // asterisk
            if (N-i>0 && i > 0) cout << "*";
            // b printing
            if (i > 0){
                cout << b;
                if (i > 1) cout << "^" << i;
            }


            if (i < N) cout << "+";
        }

        cout << endl;
    }

    return 0;
}
