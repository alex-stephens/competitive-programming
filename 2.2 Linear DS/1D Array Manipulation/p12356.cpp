// Competitive Programming 3
// Problem 12356

#include <stdio.h>

int left[100002], right[100002];

int main() {
    int S, B, L, R;

    while(1){
        scanf("%d %d", &S, &B);
        if (S == 0 && B == 0){
            break;
        }

        for (int i = 1; i < S+1; i++){
            left[i] = i-1;
            right[i] = i+1;
        }

        right[S] = 0;

        for (int i = 0; i < B; i++){
            scanf("%d %d", &L, &R);
            left[right[R]] = left[L];
            right[left[L]] = right[R];

            if (left[L] == 0){
                printf("* ");
            }
            else{
                printf("%d ", left[L]);
            }

            if (right[R] == 0){
                printf("*\n");
            }
            else{
                printf("%d\n", right[R]);
            }

        }

        printf("-\n");
    }


}
