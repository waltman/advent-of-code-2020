CPP = /usr/bin/c++
INCLDIRS =
LIBDIRS =
LIBS =
CFLAGS = -std=c++17 -Wall -O3 $(INCLDIRS)
OBJECTS = crab_cups.o

all: crab_cups

%.o: %.cpp
	$(CPP) $(CFLAGS) -c $<

crab_cups.o: LinkedList.h

crab_cups: $(OBJECTS)
	$(CPP) -o $@ $(OBJECTS) $(LIBDIRS) $(LIBS)

clean:
	rm -f *~
	rm -f *.o
	rm -f crab_cups
