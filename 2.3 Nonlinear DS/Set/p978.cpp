// Competitive Programming 3
// Problem 978

#include <algorithm>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <string>
using namespace std;

int main(){
    int T;
    cin >> T;

    while (T--){
        int B, SG, SB, n;
        cin >> B >> SG >> SB;

        multiset <int,  greater<int> > blue;
        multiset <int,  greater<int> > green;
        set<int>::iterator it_green;
        set<int>::iterator it_blue;
        int greenFighters[B], blueFighters[B];

        for (int i = 0; i < SG; i++){
            cin >> n;
            green.insert(n);
        }
        for (int i = 0; i < SB; i++){
            cin >> n;
            blue.insert(n);
        }

        while (SB > 0 && SG > 0){
            int numFights = min(B, min((int)green.size(), (int)blue.size()));
            it_green = green.begin();
            it_blue = blue.begin();

            for (int i = 0; i < numFights; i++){
                greenFighters[i] = *it_green;
                green.erase(it_green++);
                blueFighters[i] = *it_blue;
                blue.erase(it_blue++);

                int hit = min(greenFighters[i], blueFighters[i]);
                greenFighters[i] -= hit;
                blueFighters[i] -= hit;
            }

            for (int i = 0; i < numFights; i++){
                if (greenFighters[i] > 0)
                    green.insert(greenFighters[i]);
                else
                    SG -= 1;

                if (blueFighters[i] > 0)
                    blue.insert(blueFighters[i]);
                else
                    SB -= 1;
            }
        }

        if (SG > 0){
            cout << "green wins" << endl;
            for (it_green = green.begin(); it_green!= green.end(); it_green++)
                cout << *it_green << endl;
        }
        else if (SB > 0){
            cout << "blue wins" << endl;
            for (it_blue = blue.begin(); it_blue!= blue.end(); it_blue++)
                cout << *it_blue << endl;
        }
        else
            cout << "green and blue died" << endl;

        if (T > 0) cout << endl;
    }
    return 0;
}
