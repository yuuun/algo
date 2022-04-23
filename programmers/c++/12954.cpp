#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<long long> solution(int x, int n) {
    vector<long long> answer;
    long i;
    if (x == 0){
        for (i = 0; i < n; i++){
            answer.push_back(0);
        }
    }
    else if (x > 0){
        for (i = x; i <= x * n; i += x){
            answer.push_back(i);
        }
    }else{
        for (i = x; i >= x * n; i += x){
            answer.push_back(i);
        }
    }
    return answer;
}