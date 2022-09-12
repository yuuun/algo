#include <iostream>
#include <cmath>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>

#define endl '\n'
#define MAXN 110
using namespace std;

int arr[MAXN][MAXN];
bool visited[MAXN][MAXN];
int dx[] = {0, 1};
int dy[] = {1, 0};
int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for(int tc = 1; tc <= T; ++tc){
        int n;
        cin >> n;
        memset(visited, false, sizeof(visited));
        for (int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                cin >> arr[i][j];
            }
        }
        vector<pair<int, pair<int, int>>> candidate;
        for(int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                if (arr[i][j] == 0) continue;
                if (visited[i][j]) continue;
                queue<pair<int, int>> q;
                q.push(make_pair(i, j));
                int maxx = i, maxy = j;
                while(!q.empty()){
                    int x = q.front().first;
                    int y = q.front().second;

                    q.pop();
                    for(int k = 0; k < 2; k++){
                        int nx = x + dx[k];
                        int ny = y + dy[k];
                        if (0 <= nx && nx < n && 0 <= ny && ny < n){
                            if (!visited[nx][ny] && arr[nx][ny] != 0){
                                q.push(make_pair(nx, ny));
                                visited[nx][ny] = true;
                                maxx = max(maxx, nx);
                                maxy = max(maxy, ny);
                            }
                        }
                    }
                }
                int subX = maxx - i + 1;
                int subY = maxy - j + 1;
                candidate.push_back({subX * subY, {subX, subY}});
                
            }
            sort(candidate.begin(), candidate.end());
        }
        cout << '#' << tc << ' ' << candidate.size() << ' ';
        for(int i = 0; i < candidate.size(); i++){
            cout << candidate[i].second.first << ' ' << candidate[i].second.second << ' ';
        }
        cout << endl;
    }
}