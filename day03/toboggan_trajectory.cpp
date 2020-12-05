#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

typedef struct {
    int dc;
    int dr;
} Slope;

int num_trees(vector<string> tree_map, int num_rows, int num_cols, Slope slope) {
    int trees = 0;
    int row = 0;
    int col = 0;

    while (row < num_rows) {
        if (tree_map[row][col] == '#')
            trees++;

        row += slope.dr;
        col = (col + slope.dc) % num_cols;
    }
    return trees;
}

int main(int argc, char *argv[]) {
    const string fname = argv[1];

    ifstream infile(fname);
    if (!infile) {
        perror(fname.c_str());
        exit(1);
    }

    vector<string> tree_map;
    string line;
    while (infile >> line) {
        tree_map.push_back(line);
    }

    int num_rows = tree_map.size();
    int num_cols = tree_map[0].size();

    // Part 1
    Slope slope = {3, 1};
    cout << "Part 1: " << num_trees(tree_map, num_rows, num_cols, slope) << endl;
    
    // Part 2
    Slope slopes[] = {
        { 1, 1 },
        { 3, 1 },
        { 5, 1 },
        { 7, 1 },
        { 1, 2 },
    };

    unsigned long long tree_prod = 1;
    for (auto slope : slopes)
        tree_prod *= num_trees(tree_map, num_rows, num_cols, slope);

    cout << "Part 2: " << tree_prod << endl;
}
