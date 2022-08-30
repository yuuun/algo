// g++ 2819.cpp -std=c++11
#include<algorithm>
#include<iostream>
#include<set>
#include<queue>
#include<vector>

using namespace std;
char maps[4][4];
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, 1, -1};
set<string> set_maps;
bool bfs(int i, int j){
    queue<pair<string, pair<int, int> > > q;
    q.push({maps[i][j] + "", {i, j}});
    int move = 7;
    while (move--){
        int size = q.size();
        while (size--){
            string cur = q.front().first;
            int x = q.front().second.first;
            int y = q.front().second.second;
            q.pop();
            
            for (int k = 0; k < 4; k++){
                int nx = x + dx[k];
                int ny = y + dy[k];
                if (0 <= nx && nx < 4 && 0 <= ny && ny < 4){
                    string next_cur = cur + maps[nx][ny];
                    q.push({next_cur, {nx, ny}});
                }
                if (!move){
                    set_maps.insert(cur);
                }
            }
        }
    }
}

int main(){
    int T;
    cin >> T;
    for (int tc = 1; tc <= T; tc++){
        for (int i = 0; i < 4; i++){
            for (int j = 0; j < 4; j++){
                cin >> maps[i][j];
            }
        }
        set_maps.clear();
        
        for (int i = 0; i < 4; i++){
            for (int j = 0; j < 4; j++){
                bfs(i, j);
            }
        }
        cout << '#' << tc << ' ' << set_maps.size() << endl;
    }
    return 0;
}