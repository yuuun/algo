// longest common subsequence 알고리즘(LCS알고리즘)
#include <iostream>
#include <cstring>

#define MAXN 1001
#define endl '\n'

using namespace std;

int arr[MAXN][MAXN];

int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);
    
    memset(arr, 0, sizeof(arr));
    string x, y;
    cin >> x >> y;
    x = '0' + x;
    y = '0' + y;
    int n = x.size();
    int m = y.size();
    for(int i = 1; i < n; i++){
        for(int j = 1; j < m; j++){
            if(x[i] == y[j]){
                arr[i][j] = arr[i - 1][j - 1] + 1;
            } else {   
                if(arr[i - 1][j] > arr[i][j - 1]){
                    arr[i][j] = arr[i - 1][j];
                } else{
                    arr[i][j] = arr[i][j - 1];
                }
            }
        }
    }
    cout << arr[n - 1][m - 1];
}