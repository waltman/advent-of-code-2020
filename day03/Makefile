CPP = /usr/bin/c++
INCLDIRS =
LIBDIRS =
LIBS =
CFLAGS = -std=c++17 -Wall -O3 $(INCLDIRS)
OBJECTS = toboggan_trajectory.o

all: toboggan_trajectory

%.o: %.cpp
	$(CPP) $(CFLAGS) -c $<

toboggan_trajectory: $(OBJECTS)
	$(CPP) -o $@ $(OBJECTS) $(LIBDIRS) $(LIBS)

clean:
	rm -f *~
	rm -f *.o
	rm -f toboggan_trajectory
