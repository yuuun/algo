#include <iostream>
using namespace std;

int main(){
    for (int tc = 0; tc < 10; ++tc){
        int n;
        cin >> n;

        int res = 0;
        int arr[100][100];
        for (int i = 0; i < 100; i++){
            for (int j = 0; j < 100; j++){
                cin >> arr[i][j];
            }
        }

        for (int i = 0; i < 100; i++){
            int weightSum = 0;
            for (int j = 0; j < 100; j++){
                weightSum += arr[i][j];
            }
            if (weightSum > res){
                 res = weightSum;
            }
        }


        for (int j = 0; j < 100; j++){
            int weightSum = 0;
            for (int i = 0; i < 100; i++){
                weightSum += arr[i][j];
            }
            if (weightSum > res){
                 res = weightSum;
            }
        }

        int weightSum = 0;
        for (int i = 0, j = 0; i < 100; i++, j++){
            weightSum += arr[i][j];    
        }
        if (weightSum > res){
             res = weightSum;
        }

        weightSum = 0;
        for (int i = 0, j = 99; i < 100; i++, j--){
            weightSum += arr[i][j];    
        }
        if (weightSum > res){
            res = weightSum;
        }

        cout << '#' << n << ' ' << res << endl;
    }
}