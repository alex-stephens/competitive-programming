// Competitive Programming 3
// Problem 10491

#include <iostream>
#include <cstring>
using namespace std;

int main(){
    int y, n, show, tot; // y = car, n = cow, n = show
    double p_win;
    while (cin >> n){
        cin >> y >> show;
        tot = y + n;
        p_win = (double) (y * (y-1+n)) / (tot * (tot - show - 1));
        printf("%.5lf\n", p_win);
    }
    return 0;
}
