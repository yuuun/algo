#include <iostream>
using namespace std;
int main(){
    int s;
    int num = 1;
    long long sum = 0;
    int cnt = 0;
    cin >> s;
    while (1) {
		sum = sum + num;
		cnt++;
		if (sum > s) {
			cnt--;
			break;
		}
		num++;
	}
    cout << cnt << endl;
}