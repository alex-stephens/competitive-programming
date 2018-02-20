// Competitive Programming 3
// Problem 10226

#include <map>
#include <string>
#include <cstring>
#include <iostream>
using namespace std;

int main(){
    int T;
    char name[30];
    scanf("%d\n\n", &T);

    while (T--){
        int num = 0;
        map<string, int> dict;

        while (gets(name)){
            if (strlen(name) == 0) break;

            if (dict.count(string(name)) == 0){
                dict[string(name)] =1;
            }
            else{
                dict[string(name)]++;
            }
            num++;
        }

        map<string, int>::iterator it;
        for (it = dict.begin(); it != dict.end(); it++) {
			printf("%s %.4lf\n", (*it).first.data(),
					(double) ((*it).second * 100.0) / (double) num );
		}

        if (T > 0){
            dict.clear();
            cout << endl;
        }
    }
    return 0;
}
