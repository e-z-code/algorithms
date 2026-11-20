#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll INF = (1LL << 62);

int main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // 1. TO GET THE INPUT

    int node_cnt, edge_cnt, shortcut_cnt;
    cin >> node_cnt >> edge_cnt >> shortcut_cnt;

    vector<vector<pair<int, ll>>> graph(node_cnt);
    vector<vector<pair<int, ll>>> shortcut(node_cnt);

    for (int edge = 0; edge < edge_cnt; edge++) {

        int nodeA, nodeB;
        ll dist, shortcut_dist;

        cin >> nodeA >> nodeB >> dist >> shortcut_dist;
        nodeA--;
        nodeB--;

        graph[nodeA].push_back({nodeB, dist});
        graph[nodeB].push_back({nodeA, dist});
        if (shortcut_dist != -1) {
            shortcut[nodeA].push_back({nodeB, shortcut_dist});
            shortcut[nodeB].push_back({nodeA, shortcut_dist});
        }

    }

    // 2. TO SOLVE THE PROBLEM - DIJKSTRA

    vector<vector<ll>> min_dist(node_cnt, vector<ll>(shortcut_cnt + 1, INF));
    min_dist[0][0] = 0;

    using State = tuple<ll, int, int>;
    priority_queue<State, vector<State>, greater<State>> heap;
    heap.push({0, 0, 0});

    while (!heap.empty()) {

        auto [now_dist, now_used, now_node] = heap.top();
        heap.pop();

        if (now_dist <= min_dist[now_node][now_used]) {
            for (auto [next_node, add_dist] : graph[now_node]) {
                ll next_dist = now_dist + add_dist;
                if (next_dist < min_dist[next_node][now_used]) {
                    heap.push({next_dist, now_used, next_node});
                    for (int shortcut_used = now_used; shortcut_used <= shortcut_cnt; shortcut_used++) {
                        min_dist[next_node][shortcut_used] = min(min_dist[next_node][shortcut_used], next_dist);
                    }
                }
            }
            if (now_used < shortcut_cnt) {
                for (auto [next_node, add_dist] : shortcut[now_node]) {
                    ll next_dist = now_dist + add_dist;
                    if (next_dist < min_dist[next_node][now_used + 1]) {
                        heap.push({next_dist, now_used + 1, next_node});
                        for (int shortcut_used = now_used + 1; shortcut_used <= shortcut_cnt; shortcut_used++) {
                            min_dist[next_node][shortcut_used] = min(min_dist[next_node][shortcut_used], next_dist);
                        }
                    }
                }
            }
        }
    }

    ll answer = INF;
    for (int shortcut_used = 0; shortcut_used <= shortcut_cnt; shortcut_used++) {
        answer = min(answer, min_dist[node_cnt - 1][shortcut_used]);
    }
    cout << answer << '\n';

    return 0;
}