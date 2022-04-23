#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool solution(string s) {
    if (s.length() != 4 && s.length() != 6){
        return false;
    }
    bool answer = true;
    for (int i = 0; i < s.length(); i++){
        if ((s[i] >= '1' && s[i] <= '9')||s[i] == '0'){
            continue;
        }
        else{
            answer = false;
            break;
        }
    }
    return answer;
}