// Competitive Programming 3
// Problem 1203

#include <algorithm>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <queue>

using namespace std;

template<typename T> void print_queue(T& q) {
    while(!q.empty()) {
        std::cout << q.top() << " ";
        q.pop();
    }
    std::cout << '\n';
}

// priority: first by time, then Qnum. Period must be known

int main(){
    char reg[20];
    string line;
    int Qnum, period;
    priority_queue <int, vector<int>, greater<int> > q;
    <int, vector<int>, greater<int> > iterator it = q.begin();

    while ((cin >> line) && line != "#" ){
        cin >> Qnum >> period;
        cout << Qnum << "  " << period << endl;

        q.push((1));
    }

    print_queue(q);


    return 0;
}
