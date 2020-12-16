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

int do_turn(LastInfo *last_seen, int t, int last) {
    LastInfo li = last_seen[last];
    int next_val;
    if (li.second == -1)
        next_val = 0;
    else
        next_val = li.second - li.first;

    if (last_seen[next_val].first >= 0) {
        LastInfo old_li = last_seen[next_val];
        int i = (old_li.second > 0) ? old_li.second : old_li.first;
        last_seen[next_val] = {i, t};
    } else
        last_seen[next_val] = {t, -1};

    return next_val;
}
            

int main(int argc, char *argv[]) {
    vector<string> v = vec_split(argv[1], ',');
    LastInfo *last_seen = new LastInfo[30000000];
    for (int t = 0; t < 30000000; t++)
        last_seen[t] = {-1,-1};
    
    for (size_t t = 0; t < v.size(); t++) {
        LastInfo li = {(int) t+1, -1};
        last_seen[atoi(v[t].c_str())] = li;
    }

    int last = 0;
    for (int t = v.size()+1; t <= 2020; t++)
        last = do_turn(last_seen, t, last);
    cout << "Part 1: " << last << endl;

    for (int t = 2021; t <= 30000000; t++)
        last = do_turn(last_seen, t, last);
    cout << "Part 1: " << last << endl;
}
