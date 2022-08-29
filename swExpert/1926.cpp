#include<iostream>
#include<string> // stoi()
using namespace std;

int main(){
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++){
        string str = to_string(i);
        int cnt = 0;
        for (int j = 0; j < str.size(); j++){
            int k = int(str[j]) - 48;
            if (k == 3 || k == 6 || k == 9){
                cnt += 1;
            }
        }
        if (cnt == 0){
            cout << i;
        } else{
            for (int j = 0; j < cnt; j++){
                cout << '-';
            }
        }
        cout << ' ';
    }
}