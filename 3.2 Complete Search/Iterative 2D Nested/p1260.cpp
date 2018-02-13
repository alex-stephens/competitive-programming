// Competitive Programming 3
// Problem 927

#include <iostream>

using namespace std;

int main(){
    int T;
    cin >> T;

    while(T--){
        int N, count = 0;
        cin >> N;
        int A[N];

        for (int i = 0; i < N; i++)
            cin >> A[i];

        for (int i = 1; i < N; i++){
            for (int j = 0; j < i; j++){
                if (A[i] >= A[j])
                    count += 1;
            }
        }
        cout << count << endl;
    }
    return 0;
}
