#include <string>
#include <vector>

using namespace std;

long long solution(int a, int b) {
    if (a > b){
        int tmp = a;
        a = b;
        b = tmp;
    }
    long long answer = 0;
    for (int k = a; k <= b; k++){
        answer += k;
    }
    return answer;
}