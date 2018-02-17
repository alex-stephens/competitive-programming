// Competitive Programming 3
// Problem 11926

#include <iostream>
#include <cstring>
using namespace std;

int main(){
    while (1){
        int m, n;
        cin >> n >> m;
        if (m == 0 && n == 0) break;

        bool result = true;
        bool A[1000000];    // available
        memset(A, true, 1000000);

        while (n--){
            int start, end;
            cin >> start >> end;

            for (int i = start; i < end; i++){
                if (!A[i]){
                    result = false;
                    break;
                }
                else
                    A[i] = false;
            }
        }

        while (m--){
            int start, end, x;
            cin >> start >> end >> x;
            int interval = 0;

            while (start + interval < 1000000 && result){
                for (int i = start+interval; i < min(end+interval,1000000); i++){
                    if (!A[i]){
                        result = false;
                        break;
                    }
                    else
                        A[i] = false;
                }
                interval += x;
            }
        }

        if (result) printf("NO CONFLICT\n");
        else printf("CONFLICT\n");
    }
    return 0;
}
