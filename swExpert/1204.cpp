#include<iostream>
using namespace std;
int main(){
    int T;
    cin >> T;
    for(int tc = 0; tc < T; ++tc){
        int n;
        cin >> n;
        int scoreCnt[101] = {0, };
        for (int i = 0; i < 1000; i++){
            int score;
            cin >> score;
            scoreCnt[score] += 1;
        }
        
        int maxIdx = 0, maxValue = 0;
        for (int i = 100; i >= 0; --i){
            if (scoreCnt[i] > maxValue){
                maxIdx = i;
                maxValue = scoreCnt[i];
            }
        }

        cout << "#" << n << " " << maxIdx << endl;
    }
}