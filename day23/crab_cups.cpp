#include <stdlib.h>
#include <string.h>
#include <iostream>
#include "LinkedList.h"

using namespace std;

void usage() {
    cout << "crab_cubs N MOVES [12] INPUT" << endl;
    exit(0);
}

LinkedList *create_circle_list(const unsigned long long n, const char *init) {
    LinkedList *cups = new LinkedList[n];
    const size_t initlen = strlen(init);
    
    // initialize values
    for (unsigned long long i = 0; i < n; i++)
        cups[i].set_val(i+1);

    // link all but the last digit in init
    for (size_t i = 0; i < initlen - 1; i++)
        cups[init[i]- '0' - 1].set_next(cups + init[i+1] - '0' - 1);

    // link from initlen to n-1
    for (size_t i = initlen; i < n; i++)
        cups[i].set_next(cups + i + 1);
                                   
    // now complete the circle
    if (n == strlen(init))
        cups[init[n-1] - '0' - 1].set_next(cups + init[0] - '0' - 1);
    else {
        cups[init[strlen(init)-1] - '0' - 1].set_next(cups + initlen);
        cups[n-1].set_next(cups + init[0] - '0' - 1);
    }

    return cups;
}

void do_move(LinkedList *cups, LinkedList *cup, const unsigned long long N) {
    // bypass the next 3 nodes
    LinkedList *front = cup->next();
    LinkedList *back = front->next()->next();
    cup->set_next(back->next());

    // which values were just picked?
    unsigned long long picked[3] = {front->val(), front->next()->val(), back->val()};

    // find the destination value
    unsigned long long dest = cup->val() - 1;
    if (dest == 0)
        dest = N;

    while (1) {
        bool found = false;
        for (int i = 0; i < 3; i++) {
            if (picked[i] == dest) {
                dest--;
                if (dest == 0)
                    dest = N;
                found = true;
                break;
            }
        }
        if (!found)
            break;
    }

    // find the destination node
    LinkedList *p = cups + dest - 1;

    // insert the picked notes at p
    back->set_next(p->next());
    p->set_next(front);
}

void part1(LinkedList *cups) {
    LinkedList *p = cups->next();
    int score = 0;
    for (int i = 0; i < 8; i++) {
        score *= 10;
        score += p->val();
        p = p->next();
    }

    cout << "Part 1: " << score << endl;
}

void part2(LinkedList *cups) {
    cout << "Part 2: " << cups->next()->val() * cups->next()->next()->val() << endl;
}

int main(int argc, char *argv[]) {
    if (argc != 5) {
        cout << "argc == " << argc << endl;
        usage();
    }
    
    const unsigned long long N = atoi(argv[1]);
    const int MOVES = atoi(argv[2]);
    const int part = atoi(argv[3]);
    const char *init = argv[4];

    LinkedList *cups = create_circle_list(N, init);
    LinkedList *cup = cups + init[0] - '0' - 1;
    for (int i = 0; i < MOVES; i++) {
        do_move(cups, cup, N);
        cup = cup->next();
    }

    if (part == 1)
        part1(cups);
    else if (part == 2)
        part2(cups);
}
