#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<ll, ll> frac_t;
typedef pair<double, double> range_t;

const double INF = numeric_limits<double>::infinity();


// 2. UTILITY FUNCTIONS

ll car_width, crosswalk_length;
vector<pair<ll, ll>> people;

frac_t frac(ll num, ll den) {
    ll div = gcd(num, den);
    return {num / div, den / div};
}

ll my_floor(ll num, ll den) {
    if (num >= 0) return num / den;
    else return (num - den + 1) / den;
}

ll my_ceil(ll num, ll den) {
    if (num % den == 0) return num / den;
    else return my_floor(num, den) + 1;
}


// 3. FUNCTIONS TO GET VALID RANGE

vector<range_t> get_crosswalk_time(int i) {
    
    ll a = people[i].second;
    ll b = people[i].first;

    if (a == 0) {
        if (0 <= b && b <= crosswalk_length) {
            return {{0, INF}};
        }
    } else {
        double timeA = max(0.0, - double(b) / a);
        double timeB = max(0.0, double(crosswalk_length - b) / a);
        if (a > 0 && timeB != 0.0) {
            return {{timeA, timeB}};
        } else if (a < 0 && timeA != 0.0) {
            return {{timeB, timeA}};
        }
    }

    return {};
}

vector<range_t> get_safe_time(int i, int j) {
    
    vector<range_t> safe_time;

    ll a1 = people[i].second;
    ll b1 = people[i].first;
    ll a2 = people[j].second;
    ll b2 = people[j].first;

    if (a1 < a2) {
        swap(b1, b2);
        swap(a1, a2);
    }

    if (a1 == a2) {
        if (abs(b1 - b2) >= car_width) {
            safe_time.push_back({0, INF});
        }
    } else {
        ll upper_bound = my_floor(b2 - b1 - car_width, a1 - a2);
        if (0 <= upper_bound) {
            safe_time.push_back({0, (double) upper_bound});
        }
        ll lower_bound = my_ceil(b2 - b1 + car_width, a1 - a2);
        safe_time.push_back({max(0.0, (double) lower_bound), INF});
    }

    return safe_time;
    
}

pair<frac_t, frac_t> get_event(int i, int j) {
    
    ll a1 = people[i].second;
    ll b1 = people[i].first;
    ll a2 = people[j].second;
    ll b2 = people[j].first;

    if (a1 != a2 && b1 != b2) {
        ll num = b1 - b2;
        ll den = a2 - a1;
        if (den < 0) {
            num = -num;
            den = -den;
        }
        frac_t time = frac(num, den);
        frac_t place = frac(a1 * num + den * b1, den);
        return {time, place};
    } else {
        return {{0, 0}, {0, 0}};
    }
    
}

vector<range_t> range_intersect(const vector<range_t>& rangeA, const vector<range_t>& rangeB) {
    
    vector<range_t> result;

    int i = 0, j = 0;
    while (i < (int)rangeA.size() && j < (int)rangeB.size()) {
        double left = max(rangeA[i].first, rangeB[j].first);
        double right = min(rangeA[i].second, rangeB[j].second);
        if (left <= right) {
            result.push_back({left, right});
        }

        if (rangeA[i].second < rangeB[j].second) {
            i += 1;
        } else {
            j += 1;
        }
    }

    return result;
    
}

vector<range_t> sweep_range(const vector<range_t>& ranges) {
    
    if (ranges.empty()) {
        return {};
    }

    vector<range_t> result;

    double now_left = ranges[0].first, now_right = ranges[0].second;
    for (int idx = 1; idx < (int) ranges.size(); idx++) {
        double left = ranges[idx].first, right = ranges[idx].second;
        if (left <= now_right) {
            now_right = max(now_right, right);
        } else {
            result.push_back({now_left, now_right});
            now_left = left;
            now_right = right;
        }
    }

    result.push_back({now_left, now_right});
    return result;
    
}


int main() {
    
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // 1. TO GET THE INPUT

    int people_count;
    cin >> people_count >> car_width >> crosswalk_length;

    people = {{0, 0}, {crosswalk_length, 0}};
    for (int person = 0; person < people_count; person++) {
        // y = ax + b
        ll a, b;
        cin >> b >> a;
        people.push_back({b, a});
    }

    people_count += 2;
    sort(people.begin(), people.end());


    // 4. TO GET CROSSWALK TIME FOR EACH LINE

    vector<vector<range_t>> crosswalk_time(people_count);
    for (int i = 0; i < people_count; i++) {
        crosswalk_time[i] = get_crosswalk_time(i);
    }


    // 5. TO GET EVENTS

    map<pair<frac_t, frac_t>, set<int>> events;

    for (int i = 0; i < people_count; i++) {
        for (int j = i + 1; j < people_count; j++) {
            auto [time, place] = get_event(i, j);
            if (time.first > 0) {
                if (events.find({time, place}) != events.end()) {
                    events[{time, place}].insert(i);
                    events[{time, place}].insert(j);
                } else {
                    events[{time, place}] = {i, j};
                }
            }
        }
    }

    vector<pair<frac_t, frac_t>> time_order;
    for (auto& entry : events) {
        time_order.push_back(entry.first);
    }
    sort(time_order.begin(), time_order.end(), [](const pair<frac_t, frac_t>& key1, const pair<frac_t, frac_t>& key2) {
        ll num1 = key1.first.first, den1 = key1.first.second;
        ll num2 = key2.first.first, den2 = key2.first.second;
        return (__int128) num1 * den2 < (__int128) num2 * den1;
    });


    // 6. TO GET NEIGHBORING TIME OF TWO LINES

    vector<int> person_to_rank(people_count);
    vector<int> rank_to_person(people_count);
    for (int person = 0; person < people_count; person++) {
        person_to_rank[person] = person;
        rank_to_person[person] = person;
    }

    map<pair<int, int>, vector<double>> neighboring_time;
    for (int idx = 0; idx < people_count - 1; idx++) {
        neighboring_time[{idx, idx + 1}] = {0};
    }

    vector<pair<int, int>> stack;

    for (int idx = 0; idx < (int)time_order.size(); idx++) {
        
        auto event_info = time_order[idx];
        frac_t time = event_info.first;
        frac_t place = event_info.second;

        // To find ranks to reverse
        int min_rank = INT_MAX, max_rank = INT_MIN;
        for (int person : events[event_info]) {
            min_rank = min(min_rank, person_to_rank[person]);
            max_rank = max(max_rank, person_to_rank[person]);
        }
        stack.push_back({min_rank, max_rank});

        if (idx == (int) time_order.size() - 1 || time_order[idx + 1].first != time) {
            
            // Disconnect
            set<pair<int, int>> disconnect_set;
            for (auto [mr, mxr] : stack) {
                if (mr != 0) {
                    int personA = rank_to_person[mr - 1], personB = rank_to_person[mr];
                    if (personA > personB) {
                        swap(personA, personB);
                    }
                    disconnect_set.insert({personA, personB});
                }
                if (mxr != people_count - 1) {
                    int personA = rank_to_person[mxr], personB = rank_to_person[mxr + 1];
                    if (personA > personB) {
                        swap(personA, personB);
                    }
                    disconnect_set.insert({personA, personB});
                }
            }
            for (auto [personA, personB] : disconnect_set) {
                if (neighboring_time.find({personA, personB}) != neighboring_time.end()) {
                    neighboring_time[{personA, personB}].push_back((double) my_floor(time.first, time.second));
                } else {
                    neighboring_time[{personA, personB}] = {(double) my_floor(time.first, time.second)};
                }
            }

            // Reverse rank
            for (auto [mr, mxr] : stack) {
                for (int rank = mr; rank < (mr + mxr + 1) / 2; rank++) {
                    int rankA = rank, rankB = mr + mxr - rank;
                    int personA = rank_to_person[rankA], personB = rank_to_person[rankB];
                    swap(person_to_rank[personA], person_to_rank[personB]);
                    swap(rank_to_person[rankA], rank_to_person[rankB]);
                }
            }

            // Connect
            set<pair<int, int>> connect_set;
            for (auto [mr, mxr] : stack) {
                if (mr != 0) {
                    int personA = rank_to_person[mr - 1], personB = rank_to_person[mr];
                    if (personA > personB) {
                        swap(personA, personB);
                    }
                    connect_set.insert({personA, personB});
                }
                if (mxr != people_count - 1) {
                    int personA = rank_to_person[mxr], personB = rank_to_person[mxr + 1];
                    if (personA > personB) {
                        swap(personA, personB);
                    }
                    connect_set.insert({personA, personB});
                }
            }
            for (auto [personA, personB] : connect_set) {
                if (neighboring_time.find({personA, personB}) != neighboring_time.end()) {
                    neighboring_time[{personA, personB}].push_back((double) my_ceil(time.first, time.second));
                } else {
                    neighboring_time[{personA, personB}] = {(double) my_ceil(time.first, time.second)};
                }
            }

            stack.clear();
        }
    }

    map<pair<int, int>, vector<range_t>> neighboring_ranges;
    
    for (auto& entry : neighboring_time) {
        
        auto key = entry.first;
        auto& vec = entry.second;

        int length = vec.size();
        if (length % 2 == 1) {
            vec.push_back(INF);
            length += 1;
        }

        vector<range_t> result;
        for (int idx = 0; idx < length; idx += 2) {
            result.push_back({vec[idx], vec[idx + 1]});
        }
        neighboring_ranges[key] = result;
    
    }


    // 7. TO SOLVE THE PROBLEM

    vector<range_t> valid_range;
    for (auto& entry : neighboring_ranges) {
        
        int i = entry.first.first;
        int j = entry.first.second;
        auto& neigh_ranges = entry.second;
        auto valid = range_intersect(
            range_intersect(get_safe_time(i, j), neigh_ranges),
            range_intersect(crosswalk_time[i], crosswalk_time[j])
        );
        if (!valid.empty()) {
            valid_range.insert(valid_range.end(), valid.begin(), valid.end());
        }
        
    }
    sort(valid_range.begin(), valid_range.end());
    valid_range = sweep_range(valid_range);

    int now_idx = 0;
    int query_count;
    cin >> query_count;
    for (int query = 0; query < query_count; query++) {
        ll time;
        cin >> time;
        while (true) {
            if (time > valid_range[now_idx].second) {
                now_idx += 1;
                if (now_idx == (int)valid_range.size()) {
                    cout << "N\n";
                    break;
                }
            } else if (time < valid_range[now_idx].first) {
                cout << "N\n";
                break;
            } else {
                cout << "Y\n";
                break;
            }
        }
    }

    return 0;
}
