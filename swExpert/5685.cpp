#include <iostream>

using namespace std;

int arr[100];
long long cnt = 0;
int n;
void dfs(int idx, int cur){
    if (idx == n - 1){
        if(arr[n - 1] == cur){
            cnt += 1;
        }
        return;
    }
    if (cur < 0 || cur > 20){
        return;
    }
    dfs(idx + 1, cur + arr[idx]);
    dfs(idx + 1, cur - arr[idx]);
}
int main(){
    int T;
    cin >> T;
    for(int tc = 1; tc <= T; tc++){
        cin >> n;
        for(int i = 0; i < n; i++){
            cin >> arr[i];
        }
        dfs(1, arr[0]);
        cout << '#' << tc << ' ' << cnt % 1234567891 << endl;
    }
}

