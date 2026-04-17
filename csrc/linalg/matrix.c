#include <stdio.h>
#include <math.h>
#include <stdlib.h>


typedef struct {
    int rows, cols;
    float* data;
} matrix;

/*
 // Not really using this rn

typedef struct {
    matrix mat;
    int size;
} mat_obj;

void set_mat(mat_obj* m, float* data);
*/


void init_matrix(matrix* m, float* data, int size);
int set_val(matrix* m, int r, int c, float val);
float get_val(const matrix* m, int r, int c);

int main() {
    matrix mat;
    int r = 2;
    int c = 3;

    float data[6] = {0.0, 1.0, 2.0, 3.0, 4.0, 5.0};

    mat.data = malloc(r*c*sizeof(float));
    mat.rows = r;
    mat.cols = c;

    init_matrix(&mat, data, mat.rows*mat.cols);

    for (int i=0; i<r*c; ++i)
        printf("mat[%d] = %.2f\n", i, mat.data[i]);

    free(mat.data);

    return 0;
}

/*
void set_mat(mat_obj* m, float* data) {
    for (int i=0; i < m->size; ++i) 
        m->mat.data[i] = data[i];
}
*/

void init_matrix(matrix* m, float* data, int size) {
    if (size != m->rows*m->cols)
        EXIT_FAILURE;

    for (int i=0; i<size; ++i) {
        m->data[i] = data[i];
    }
}

int set_val(matrix* m, int r, int c, float val) {
    if (r < 0 || r >= m->rows || c < 0 || c >= m->cols) {
        fprintf(stderr, "ERROR: Matrix out of bounds. Ignoring and returning");
        return 0;
    }

    int offset = r*m->cols + c;

    m->data[offset] = val;

    return 1;
}

float get_val(const matrix* m, int r, int c) {
    if (r < 0 || r >= m->rows || c < 0 || c >= m->cols) {
        fprintf(stderr, "FATAL ERROR: Matrix out of bounds.");
        exit(EXIT_FAILURE);
    }

    int offset = r*m->cols + c;
    return m->data[offset];
}