#include <iostream>
#define MAX 101
#include <queue>
using namespace std;
int map[101][101] = {0,};
bool visited[101] = {0,};
int main(){
    int n, v;
    cin >> n;
    cin >> v;
    for (int i = 0; i < v; i++){
        int a, b;
        cin >> a >> b;
        map[a][b] = 1;
        map[b][a] = 1;
    }
    visited[1] = true;
    queue<int> q;
    q.push(1);
    int cnt = 0;
    while (!q.empty()){
        v = q.front();
        q.pop();
        for (int i = 1; i <= n; i++){
            if (map[v][i] == 1 && visited[i] == 0){
                q.push(i);
                visited[i] = true;
                cnt++;
            }
        }
    }
    cout << cnt << endl;
}