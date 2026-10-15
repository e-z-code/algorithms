#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using State = tuple<ll, int, ll>;

vector<priority_queue<State, vector<State>, greater<State>>> graph;

// 2. DFS FUNCTION TO SOLVE THE PROBLEM

void solve(int node, ll val) {

    if (!(graph[node].empty())) {

        auto [now_total_val, next_node, edge_val] = graph[node].top();
        graph[node].pop();

        solve(next_node, val);

        ll next_total_val;
        if (!graph[next_node].empty()) {
            next_total_val = get<0>(graph[next_node].top()) + edge_val + val;
        } else {
            next_total_val = edge_val + val;
        }

        graph[node].push({next_total_val, next_node, edge_val + val});
    }

}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // 1. TO GET THE INPUT

    int factor, level, mission_cnt;
    cin >> factor >> level >> mission_cnt;

    vector<ll> missions(mission_cnt);
    for (int mission = 0; mission < mission_cnt; mission++) {
        cin >> missions[mission];
    }

    ll node_cnt;
    if (factor == 1) {
        node_cnt = level;
    } else {
        ll power = 1;
        for (int i = 0; i < level; i++) {
            power *= factor;
        }
        node_cnt = (power - 1) / (factor - 1);
    }

    int now_parent = 0;
    int now_child = 1;

    graph.resize(node_cnt);
    while (now_child < node_cnt) {
        graph[now_parent].push({0, now_child, 0});
        if ((int)graph[now_parent].size() == factor) {
            now_parent++;
        }
        now_child++;
    }

    // 3. TO SOLVE THE PROBLEM

    for (ll mission : missions) {
        solve(0, mission);
    }
    cout << get<0>(graph[0].top()) << '\n';

    return 0;
}