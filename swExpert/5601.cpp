#include <iostream>

using namespace std;

int main(){
    int T;
    cin >> T;
    for (int tc = 1; tc <= T; tc++){
        int n;
        cin >> n;
        cout << "#" << tc << ' ';
        for (int i = 0; i < n; i++){
            cout << 1 << '/' << n << ' ';
        }
        cout << endl;
    }
}