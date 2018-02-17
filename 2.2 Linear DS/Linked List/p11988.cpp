// Competitive Programming 3
// Problem 11926

#include <iostream>
#include <cstring>
#include <string>
#include <list>
using namespace std;

int main(){
    string input;
    input.reserve(100005);

    while (cin >> input){
        list<char> output = {};
        list<char>::iterator i;
        i = output.begin();

        // iterate through the input
        for(char c : input) {
            if (c == '[')
                i = output.begin();
            else if (c == ']')
                i = output.end();
            else if (i == output.end())
                output.push_back(c);
            else {
                output.insert(i, c);
            }
        }
        // print output
        for (char c : output){
            cout << c;
        }
        cout << endl;
    }
    return 0;
}
