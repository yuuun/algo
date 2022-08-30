#include <iostream>
#include <vector>
#include <string.h>
#include <string>

using namespace std;

int main(){
    int T;
    cin >> T;
    
    int score[100];
    bool visited[10001];
    vector <int> candidate;

    for(int tc = 1; tc <= T; tc++){
        candidate.clear();
        memset(score, 0, sizeof(score));
        memset(visited, false, sizeof(visited));
        
        int n;
        cin >> n;

        for (int i = 0; i < n; i++){
            cin >> score[i];
        }
        
        visited[0] = true;
        candidate.push_back(0);
        
        for (int i = 0; i < n; i++) {
            int v_size = candidate.size();
 
            for (int j = 0; j < v_size; j++) {
                int newScore = candidate[j] + score[i];
                if (!visited[newScore]) {
                    candidate.push_back(newScore);
                    visited[newScore] = true;
                }
            }
        }
        cout << '#' << tc << ' ' << candidate.size() << endl;
    }
}