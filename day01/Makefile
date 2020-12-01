CPP = /usr/bin/c++
INCLDIRS =
LIBDIRS =
LIBS =
CFLAGS = -std=c++17 -Wall -O3 $(INCLDIRS)
OBJECTS = report_repair.o

all: report_repair

%.o: %.cpp
	$(CPP) $(CFLAGS) -c $<

report_repair: $(OBJECTS)
	$(CPP) -o $@ $(OBJECTS) $(LIBDIRS) $(LIBS)

clean:
	rm -f *~
	rm -f *.o
	rm -f report_repair
