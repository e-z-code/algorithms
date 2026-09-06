#include <bits/stdc++.h>
using namespace std;
const long long MOD = 1000000007;


// 3. FAST POWER

long long fast_pow(long long base, long long exp, long long mod) {

    if (exp == 0) {
        return 1;
    }
    else if (exp == 1) {
        return base % mod;
    }
    else {
        long long key = fast_pow(base, exp / 2, mod);
        if (exp % 2 == 0) {
            return key * key % mod;
        }
        else {
            return key * key % mod * base % mod;
        }
    }
}


// 1. PREPROCESSING - POSSIBLE CASES

int main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<long long> valid = {0, 0, 0};
    for (int num = 3; num <= 1000000; num++) {
        valid.push_back(
            (valid.back() + (num - 1) / 2) % MOD
        );
    }

    vector<long long> choose_three = {0, 0, 0};
    for (long long num = 3; num <= 1000000; num++) {
        choose_three.push_back(
            num * (num - 1) * (num - 2) / 6 % MOD
        );
    }


    // 2. TO GET THE INPUT AND SOLVE THE PROBLEM

    long long ans = 1;

    int test_cnt;
    cin >> test_cnt;

    for (int test = 0; test < test_cnt; test++) {
        int N;
        cin >> N;
        ans = (ans * valid[N] % MOD * fast_pow(choose_three[N], MOD - 2, MOD)) % MOD;
        cout << ans << '\n';
    }

    return 0;
}