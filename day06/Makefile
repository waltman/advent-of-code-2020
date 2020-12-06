CPP = /usr/bin/c++
INCLDIRS =
LIBDIRS =
LIBS =
CFLAGS = -std=c++17 -Wall -O3 $(INCLDIRS)
OBJECTS = custom_customs.o

all: custom_customs

%.o: %.cpp
	$(CPP) $(CFLAGS) -c $<

custom_customs: $(OBJECTS)
	$(CPP) -o $@ $(OBJECTS) $(LIBDIRS) $(LIBS)

clean:
	rm -f *~
	rm -f *.o
	rm -f custom_customs
