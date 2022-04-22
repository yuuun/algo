#include <iostream>
#include <queue>
using namespace std;
#define MAX 1001
int maps[MAX][MAX];
bool visited[MAX];
int n, m, V;

void init(){
    for (int i = 1; i <= n; i++){
        visited[i] = false;
    }
}
void dfs(int v){
    visited[v] = true;
    cout << v << ' ';
    for (int i = 1; i <= n; i++){
        if (maps[v][i] == 1 && visited[i] == 0){
            dfs(i);
        }
    }
}

void bfs(int v){
    queue<int> q;
    q.push(v);
    visited[v] = true;
    cout << v << ' ';
    while (!q.empty()){
        v = q.front();
        q.pop();
        for (int i = 1; i <= n; i++){
            if (maps[v][i] == 1 && visited[i] == 0){
                visited[i] = true;
                q.push(i);
                cout << i << ' ';
            }
        }
    }
}

int main(){
    cin >> n >> m >> V;
    for (int i = 0; i < m; i++){
        int a, b;
        cin >> a >> b;
        maps[a][b] = 1;
        maps[b][a] = 1;
    }
    init();
    dfs(V);
    cout << '\n';
    init();
    bfs(V);
    cout << '\n';
}