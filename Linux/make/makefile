
all: main.o helper.o
	gcc main.o helper.o -o main

main.o:
	gcc -c main.c

helper.o:
	gcc -c helper.c

clean:
	rm *.o main