// Competitive Programming 3
// Problem 10567

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    int Q;
    string S, SS;
    cin >> S >> Q;
    
    vector< vector <int> > vv;
    vector <int>::iterator it;
    vv.resize(256); // one element per ASCII character

    // store indices for each char in corresponding vector
    for (int i = 0; i < S.size(); i++)
        vv[S[i]].push_back(i);

    while (Q--){
        cin >> SS;
        int index, start = -1, end = -1;
        bool success = true;

        for (int i = 0; i < SS.size(); i++){
            char c = SS[i];
            it = upper_bound(vv[c].begin(), vv[c].end(), end);

            if (it == vv[c].end()){
                success = false;
                break;
            }
            end =  *it;
            if (i == 0) start = *it;
        }

        if (!success)
            printf("Not matched\n");
        else
            printf("Matched %d %d\n", start, end);
    }
    return 0;
}
