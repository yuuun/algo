#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(vector<int> citations) {
    int answer = 0;
    for(int i = 0; i < citations.size(); i++){
        int cnt  = 0;
        for(int j = 0; j < citations.size(); j++){
            if(citations[i] <= citations[j])
                cnt++;
        }
        if (citations[i] < cnt){
            cnt = -1;
        }
        if(answer < cnt){
            answer = cnt;
        }
    }
    return answer;
}
int main(){
    vector<int> cit = {3, 0, 6, 1, 5};
    cout << solution(cit);
}