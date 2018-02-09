// Competitive Programming 3
// Problem 10684

#include <iostream>
using namespace std;

int main(){
    while (1){
        int N;
        cin >> N;
        if (N == 0){
            break;
        }
        int curMax = 0, ans = 0;

        int num;
        while (N--){
            cin >> num;
            curMax = max(0, curMax + num);
            ans = max(ans, curMax);
        }

        if (ans == 0){
            cout << "Losing streak." << endl;
        }
        else{
            cout << "The maximum winning streak is " << ans << "."<< endl;
        }
    }

    return 0;
}
