#include <stdlib.h>
#include <string>
#include <vector>
#include <map>
#include <iostream>
#include "util.h"

using namespace std;
bool DEBUG = false;

typedef struct {
    int first;
    int second;
} LastInfo;

int do_turn(map<int, LastInfo> &last_seen, int t, int last) {
    LastInfo li = last_seen[last];
    int next_val;
    if (li.second == -1)
        next_val = 0;
    else
        next_val = li.second - li.first;

    if (in_map(last_seen, next_val)) {
        LastInfo old_li = last_seen[next_val];
        int i = (old_li.second >= 0) ? old_li.second : old_li.first;
        last_seen[next_val] = {i, t};
    } else
        last_seen[next_val] = {t, -1};

    return next_val;
}
            

int main(int argc, char *argv[]) {
    vector<string> v = vec_split(argv[1], ',');
    map<int, LastInfo> last_seen;
    for (size_t t = 0; t < v.size(); t++) {
        LastInfo li = {(int) t+1, -1};
        last_seen[atoi(v[t].c_str())] = li;
    }

    // for (std::pair<const int, LastInfo> element : last_seen) {
    //     cout << element.first << " " << last_seen[element.first].first << " " << last_seen[element.first].second << endl;
    // }

    int last = 0;
    for (int t = v.size()+1; t <= 2020; t++)
        last = do_turn(last_seen, t, last);
    cout << "Part 1: " << last << endl;

    for (int t = 2021; t <= 30000000; t++)
        last = do_turn(last_seen, t, last);
    cout << "Part 1: " << last << endl;
}
