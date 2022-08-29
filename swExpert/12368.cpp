#include <iostream>
using namespace std;

int main(){
    int T;
    cin >> T;
    for (int tc = 1; tc <= T; ++tc){
        int a, b;
        cin >> a >> b;
        cout << (a + b) << endl;
        cout << '#' << tc << ' ' << (a + b) % 24 << endl;
    }
}