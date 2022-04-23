#include <iostream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

int solution(int left, int right) {
    int answer = 0;
    vector<int> prime;
    for (int i = 2; i <= right; i++){
        bool flag = true;
        for (int j = 0; j < prime.size(); j++){
            if (i % prime[j] == 0){
                flag = false;
                break;
            }
        }
        if (flag){
            prime.push_back(i);
        }
    }
    for (int k = left; k <= right; k++){
        int t = k;
        int cal = 1;
        for (int i = 0; i < prime.size(); i++){
            int cnt = 0;
            while (true){
                if (t % prime[i] == 0){
                    t /= prime[i];
                    cnt++;
                }
                else{
                    break;
                }
            }
            cal *= (cnt + 1); 
        }
        if (cal == 1){
            cal = 2;
        }
        cout << cal << ' '<<t << endl;
        if (cal % 2 == 0){
            answer += k;
        }else{
            answer -= k;
        }

    }
    return answer;
}