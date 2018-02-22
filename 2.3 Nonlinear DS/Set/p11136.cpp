// Competitive Programming 3
// Problem 11136

#include <algorithm>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <string>
using namespace std;

int main(){
    while (1){
        int N;
        long long totalCost = 0;    // could be large
        cin >> N;
        if (N == 0) break;
        multiset <int> bills;

        while (N--){

            int n; // new entries on current day
            cin >> n;

            while (n--){
                int x;
                cin >> x;
                bills.insert(x);
            }
            multiset <int>::iterator lowest = bills.begin();
            multiset <int>::iterator highest = --bills.end();

            totalCost += *highest - *lowest;

            bills.erase(highest); bills.erase(lowest);

        }

        cout << totalCost << endl;
    }
    return 0;
}
