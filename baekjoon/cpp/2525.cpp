#include <iostream>
using namespace std;
int main(){
    int a, b, c;
    cin >> a;
    cin >> b;
    cin >> c;
    b += c;
    while (b > 59){
        b -= 60;
        a += 1;
    }
    
    while (a > 23){
        a -= 24;
    }
    cout << a << ' ' << b << endl;
}