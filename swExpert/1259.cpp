#include <iostream>
#include <deque>
#define endl '\n'
using namespace std;

int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);

    int T;
    cin >> T;
    for(int tc = 1; tc <= T; ++tc){
        int n;
        cin >> n;
        deque <pair<int, int>> stick;
        for(int i = 0; i < n; i++){
            int front, back;
            cin >> front >> back;
            stick.push_back({front, back});
        }
        deque <pair<int, int>> arr;
        arr.push_back(stick.front());
        stick.pop_front();
        while(!stick.empty()){
            for(int i = 0; i < stick.size(); i++){
                if(arr.back().second == stick[i].first){
                    arr.push_back(stick[i]);
                    stick.erase(stick.begin() + i);
                    break;
                } else if(arr.front().first == stick[i].second){
                    arr.push_front(stick[i]);
                    stick.erase(stick.begin() + i);
                    break;
                }
            }
        }
        cout << '#' << tc << ' ';
        while(!arr.empty()){
            cout << arr.front().first << ' ' << arr.front().second << ' ';
            arr.pop_front();
        }
        cout << endl;
    }
}