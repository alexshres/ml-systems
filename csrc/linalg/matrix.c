#include <stdio.h>
#include <math.h>
#include <stdlib.h>


typedef struct {
    int rows, cols;
    float* data;
} matrix;

void set_matrix(matrix* m, float* data, int size);

int main() {
    matrix m;
    int r = 2;
    int c = 3;

    m.rows = r;
    m.cols = c;

    m.data = malloc(r * c * sizeof(float));

    return 0;
}


void set_matrix(matrix* m, float* data, int size) {

    if (size != m->rows*m->cols)
        EXIT_FAILURE;

    for (int i=0; i<size; ++i) {
        m->data[i] = data[i];
    }
}