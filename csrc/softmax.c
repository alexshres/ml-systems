#include <math.h>
#include <stdio.h>
#include <stdlib.h>


void softmax(float* input, float* output, int length) {
    /*
    Compute the softmax of the input array and store the result in the output array.
    The softmax function is defined as:
    softmax(x_i) = exp(x_i) / sum(exp(x_j)) for j in [0, length-1] 
    */

    // Compute the maximum value in the input array for numerical stability
    float max_input = input[0];

    for (int i=1; i < length; ++i) {
        if (input[i] > max_input) {
            max_input = input[i];
        }
    }

    // Compute sum for denominator
    float sum_exp = 0.0f;
    for (int i=0; i<length; ++i) {
        sum_exp += expf(input[i]-max_input);
    }

    // Compute softmax output
    for (int i=0; i<length; ++i) {
        output[i] = expf(input[i]-max_input)/sum_exp;
    }
}


int main() {
    float input[] = {1.0f, 2.0f, 3.0f};
    int length = sizeof(input) / sizeof(input[0]);
    float* output = (float*)malloc(length*sizeof(float));
    float softmax_sum = 0.0f;

    softmax(input, output, length);

    // Print the input and output arrays
    printf("Input: ");
    for (int i=0; i<length; ++i) {
        printf("%f ", input[i]);
    }

    printf("\nSoftmax Output: ");
    for (int i=0; i<length; ++i) {
        printf("%f ", output[i]);
        softmax_sum += output[i];
    }

    printf("\nSum of Softmax: %f\n", softmax_sum);

    free(output);
    return 0;
}