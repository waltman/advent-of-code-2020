#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
#include <set>

using namespace std;

const int decode_binary(const string s, const int start, const int len, const char *codes) {
    int sum = 0;
    for (int i = start, shift = len-1; i < start+len; i++, shift--)
        sum += (s[i] == codes[0] ? 0 : 1) << shift;

    return sum;
}
    
const int calc_seat_id(const int row, const int col) {
    return row * 8 + col;
}

const string seat_key(const int row, const int col) {
    return to_string(row) + "," + to_string(col);
}

int main(int argc, char *argv[]) {
    const string fname = argv[1];

    ifstream infile(fname);
    if (!infile) {
        perror(fname.c_str());
        exit(1);
    }

    string line;
    int best_id = -1;
    int min_row = 99999;
    int max_row = -1;
    set<string> seats;
    while (infile >> line) {
        int row = decode_binary(line, 0, 7, "FB");
        int col = decode_binary(line, 7, 3, "LR");
        int seat_id = calc_seat_id(row, col);

        if (seat_id > best_id)
            best_id = seat_id;
        if (row > max_row)
            max_row = row;
        if (row < min_row)
            min_row = row;

        seats.insert(seat_key(row, col));
    }
    cout << "Part 1: " << best_id << endl;

    for (int row = min_row+1; row < max_row; row++)
        for (int col = 0; col <= 7; col++)
            if (seats.find(seat_key(row, col)) == seats.end())
                cout << "Part 2: " << calc_seat_id(row, col) << endl;
}
