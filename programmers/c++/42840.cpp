#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> one = {1, 2, 3, 4, 5};
    vector<int> two = {2, 1, 2, 3, 2, 4, 2, 5};
    vector<int> three = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
    vector<int> score = {0, 0, 0};
    for (int i = 0; i < answers.size(); i++){
        if (one[i % one.size()] == answers[i]){
            score[0] += 1;
        }if (two[i % two.size()] == answers[i]){
            score[1] += 1;
        }if (three[i % three.size()] == answers[i]){
            score[2] += 1;
        }
    }
    int max_idx = 0;
    int max_val = score[0];
    vector<int> answer = {1};
    for (int i = 1; i < score.size(); i++){
        if (max_val == score[i]){
            answer.push_back(i + 1);
        }
        else if (max_val < score[i]){
            answer = {i + 1};
            max_idx = i + 1;
            max_val = score[i];
        }
    }
    return answer;
}