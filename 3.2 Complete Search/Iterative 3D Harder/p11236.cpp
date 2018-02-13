// Competitive Programming 3
// Problem 11236

#include <iostream>
using namespace std;

int main(){
    int target = 2000;

    for (int a = 1; a <= target-3; a++){
        for (int b = 1; b <= min(target-a-2, a); b++){
            for (int c = 1; c <= min(target-a-b-1, b); c++){
                int d;

                if (a*b*c <= 1000000)
                    continue;

                if ((1000000 * (a+b+c)) % (a*b*c - 1000000) == 0)
                    d = (1000000 * (a+b+c)) / (a*b*c - 1000000);
                else
                    continue;

                if (d > c || a+b+c+d > 2000)
                    continue;

                if (a * b * c * d == 1000000 * (a + b + c + d)){
                    printf("%d.%.2d %d.%.2d ", d/100,d%100,c/100,c%100);
                    printf("%d.%.2d %d.%.2d\n", b/100,b%100,a/100,a%100);
                }
            }
        }
    }
    return 0;
}
