#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;

int main(int argc, char *argv[]) {
    const string fname = argv[1];

    ifstream infile(fname);
    if (!infile) {
        perror(fname.c_str());
        exit(1);
    }

    string line;
    map<char,int> questions;
    int num_groups = 0;
    int num_all = 0;
    int group_size = 0;
    while (getline(infile, line)) {
        if (line.size() > 0) {
            group_size++;
            for (char q : line)
                questions[q]++;
        } else {
            num_groups += questions.size();
            for (const auto& [key, value] : questions)
                if (value == group_size)
                    num_all++;
            questions.clear();
            group_size = 0;
        }
    }

    cout << "Part 1: " << num_groups << endl;
    cout << "Part 2: " << num_all << endl;
}
