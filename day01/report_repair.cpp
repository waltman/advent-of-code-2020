#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {
    const string fname = argv[1];

    ifstream infile(fname);
    if (!infile) {
        perror(fname.c_str());
        exit(1);
    }

    vector<int> entries;
    int entry;
    while (infile >> entry) {
        entries.push_back(entry);
    }

    bool found = false;
    for (size_t i = 0; i < entries.size()-1 && !found; i++) {
        for (size_t j = i+1; j < entries.size() && !found; j++) {
            if (entries[i] + entries[j] == 2020) {
                cout << "Part 1: " << entries[i] * entries[j] << endl;
                found = true;
            }
        }
    }

    found = false;
    for (size_t i = 0; i < entries.size()-2 && !found; i++) {
        for (size_t j = i+1; j < entries.size()-1 && !found; j++) {
            for (size_t k = j+1; k < entries.size()-1 && !found; k++) {
                if (entries[i] + entries[j] + entries[k] == 2020) {
                    cout << "Part 2: " << entries[i] * entries[j] * entries[k] << endl;
                    found = true;
                }
            }
        }
    }
}
