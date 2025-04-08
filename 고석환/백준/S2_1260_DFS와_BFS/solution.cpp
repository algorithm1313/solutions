#include <bits/stdc++.h>
using namespace std;

int N, M, V, from, to, visited[1004];
vector<int> adj[1004];

void dfs(int here) {
  visited[here] = 1;
  cout << here << ' ';

  for (int there : adj[here]) {
    if (visited[there]) continue;

    dfs(there);
  }
}

void bfs(int start) {
  visited[start] = 1;

  queue<int> q;
  q.push(start);

  while (q.size()) {
    int here = q.front();
    q.pop();

    cout << here << ' ';

    for (int there : adj[here]) {
      if (visited[there]) continue;

      visited[there] = 1;
      q.push(there);
    }
  }
}

int main() {
  cin >> N >> M >> V;

  for (int i = 0; i < M; i++) {
    cin >> from >> to;

    adj[from].push_back(to);
    adj[to].push_back(from);
  }

  for (int i = 1; i <= N; i++) {
    sort(adj[i].begin(), adj[i].end());
  }

  dfs(V);
  cout << '\n';
  memset(visited, 0, sizeof(visited));
  bfs(V);

  return 0;
}