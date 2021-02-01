#include <string>
#include <vector>
#include <iostream>

using namespace std;

int prime_list[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 
            29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 
            71, 73, 83, 89, 97};

int solution(vector<int> arr) {
    int answer = 1;
    int number_list[101][24] = {0, };
    for(int i = 0; i < arr.size(); i++){
        int num = arr[i];
        
        for(int j = 0; j < 4; j++){
            while(num % prime_list[j] == 0){
                num /= prime_list[j];
                number_list[i][j] += 1;
            }
        }
        
        //11부터는 두번 이상 나오지 않기 떄문에 한번만 하고 for문 빠져나옴
        for(int j = 4; j < 24; j++){
            if(num % prime_list[j] == 0){
                num /= prime_list[j];
                number_list[i][j] = 1;
                break;
            }
        }
        
    }
    for(int j = 0; j < 24; j++){
        int max = 0;
        for(int i = 0; i < arr.size(); i++){
            if(number_list[i][j] > max){
                max = number_list[i][j];
            }
        }
        
        for(int k = 0; k < max; k++){
            answer *= prime_list[j];
        }
    }

    return answer;
}

int main(){
    vector<int> v = {2, 6, 8, 14};
    cout << solution(v) << "\n";
}