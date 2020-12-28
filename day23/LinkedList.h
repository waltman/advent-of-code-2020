#include <stddef.h>

class LinkedList {
private:
    unsigned long long _val;
    LinkedList *_next;

public:
    LinkedList(const unsigned long long val) { _val = val; _next = NULL; }
    LinkedList() { _val = 0; _next = NULL; }

    void set_val(unsigned long long val) { _val = val; }
    const unsigned long long val() { return _val; }
    LinkedList *next() { return _next; }
    void set_next(LinkedList *next) { _next = next; }
};
