#include <bits/stdc++.h>
using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    // 1. TO GET THE INPUT

    int node_cnt, edge_cnt;
    cin >> node_cnt >> edge_cnt;

    vector<vector<int>> graph(node_cnt);

    for (int edge = 0; edge < edge_cnt; edge++) {
        int nodeA, nodeB;
        cin >> nodeA >> nodeB;

        graph[nodeA].push_back(nodeB);
        graph[nodeB].push_back(nodeA);
    }


    // 2. TO FORM THE GROUP

    vector<int> groups;
    int group_num = 1;
    vector<int> visited(node_cnt, 0);

    for (int node = 0; node < node_cnt; node++) {
        if (!visited[node]) {

            vector<int> group = {node};
            queue<int> q;

            q.push(node);
            visited[node] = group_num;
            group_num++;

            while (!q.empty()) {
                int now_node = q.front();
                q.pop();
                for (int next_node : graph[now_node]) {
                    if (!visited[next_node]) {
                        visited[next_node] = visited[now_node];
                        group.push_back(next_node);
                        q.push(next_node);
                    }
                }
            }

            groups.insert(groups.end(), group.begin(), group.end());
        }
    }


    // 3. TO SOLVE THE PROBLEM

    vector<pair<int, int>> ans;

    for (int idx = 0; idx < node_cnt / 2; idx++) {
        int nodeA = groups[idx];
        int nodeB = groups[idx + (node_cnt + 1) / 2];
        if (visited[nodeA] != visited[nodeB]) {
            ans.push_back({nodeA, nodeB});
        }
    }

    cout << ans.size() << '\n';
    for (auto [nodeA, nodeB] : ans) {
        cout << nodeA << ' ' << nodeB << '\n';
    }

    return 0;
}