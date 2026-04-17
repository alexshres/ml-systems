# Compile softmax.c

CC = gcc
DEBUG = -g
CFLAGS = -Wall -Wextra $(DEBUG)
LDFLAGS = -lm

all: softmax

# softmax.o is implicitly created from softmax.c 
softmax: softmax.o
	$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS)

matrix: matrix.o
	$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS)

.PHONY: clean
clean:
	rm -f softmax.o softmax matrix.o matrix