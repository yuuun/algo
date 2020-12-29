#include <string>
#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

int solution(int n) {
    vector<int> vals;
    while(n > 0){
        int rest = n % 3;
        n /= 3;
        vals.push_back(rest);
    }
    int answer = 0;
    int kOf3 = pow(3, vals.size());
    for (int i = 0; i < vals.size(); i++){
        kOf3 /= 3;
        answer += kOf3 * vals.at(i);
    }
    
    return answer;
}
int main(){
    cout<< solution(45)<< "\n";
    cout << solution(125) << "\n";
}