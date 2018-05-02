// Competitive Programming 3
// Problem 11057

#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
    int rows, cols, Q, a, b;
    int H[500][500];

    while(1){
        cin >> rows >> cols;
        if (rows == 0 && cols == 0) break;
        memset(H, 0, 500*500*sizeof(H[0][0]));
        for (int i = 0; i < rows; i++)
            for (int j = 0; j < cols; j++)
                cin >> H[i][j];

        for (int i = 0; i < rows; i++){
            for (int j = 0; j < cols; j++){
                cout << H[i][j] << " ";
            }
            cout << endl;
        }

        cin >> Q;

        while (Q--){
            cin >> a >> b;
            cout << a << "   " << b << endl;


        }


    }


    return 0;
}
