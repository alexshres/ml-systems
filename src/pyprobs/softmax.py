"""
@file: softmax.py
@author: Alex Shrestha

Implementation of the numerically stable softmax and log-softmax functions.
Tests for the softmax and log-softmax functions are included in the ml-systems/tests/ directory.
"""

import numpy as np
import numpy.typing as npt


def regular_softmax(x: npt.NDArray) -> npt.NDArray:
    """
    Computes the softmax of the input w/o numerical stability adjustments.
    """

    return np.exp(x) / np.sum(np.exp(x), axis=-1, keepdims=True)


def regular_softmax_issues():
    """
    Demonstrates the numerical stability issues with the regular softmax function.
    """

    # note that np.exp(2000) and np.exp(-4000) will overflow and underflow respectively, 
    # leading to incorrect softmax outputs
    x: npt.NDArray = np.array([1.2, 2000, -4000, 0.0])

    print("Input:", x)
    print("Regular Softmax Output:", regular_softmax(x))

def stable_softmax(x: npt.NDArray) -> npt.NDArray:
    """
    Computes the numerically stable softmax of the input.
    
    This is done by subtracting the maximum value from the input before exponentiating,
    preventing overflow and underflow issues. The formula is:
    softmax(x_i) = exp(x_i - max(x)) / sum(exp(x_j - max(x))) for all j 
    """

    shifted_x = x - np.max(x, axis=-1, keepdims=True)

    return np.exp(shifted_x) / np.sum(np.exp(shifted_x), axis=-1, keepdims=True)

def corrected_softmax_issues():
    """
    Demonstrates that the stable softmax function does not suffer from numerical stability issues.
    """

    x: npt.NDArray = np.array([1.2, 2000, -4000, 0.0])

    print("Input:", x)
    print("Stable Softmax Output:", stable_softmax(x))


def log_softmax(x: npt.NDArray) -> npt.NDArray:
    """
    Computes the numerically stable log-softmax of the input.
    
    __Why log-softmax?__

    It gives us pretty nice characteristics:

    1. numerical stability
    2. gradient of log softmax becomes additive since log(a/b) = log(a) - log(b)
    3. less computations such as divisions and multiplications as addition and subtraction are cheaper 
    4. log is a monotonic function, so it preserves the order of the probabilities, which can be useful in certain applications 
        - when used for classifiers, the log-softmax has the effect of heavily penalizing incorrect predictions


    This is done by using the log-sum-exp trick, which prevents overflow and underflow issues. 
    The formula is:
    log_softmax(x_i) = x_i - max(x) - log(sum(exp(x_j - max(x)))) for all j
    """

    shifted_x = x - np.max(x, axis=-1, keepdims=True)
    return shifted_x - np.log(np.sum(np.exp(shifted_x), axis=-1, keepdims=True))

def log_softmax_to_probabilities(ls_output: npt.NDArray) -> npt.NDArray:
    """
    Converts log-softmax output back to probabilities.
    This is done by exponentiating the log-softmax output, which gives us the original probabilities.
    """

    return np.exp(ls_output) / np.sum(np.exp(ls_output), axis=-1, keepdims=True)

def corrected_log_softmax_issues():
    """
    Demonstrates that the log-softmax function does not suffer from numerical stability issues.
    """

    x: npt.NDArray = np.array([1.2, 2000, -4000, 0.0])

    print("Input:", x)
    print("Log-Softmax Output:", log_softmax(x))

    return log_softmax(x)




if __name__ == "__main__":
    print("Demonstrating Regular Softmax Issues:")
    regular_softmax_issues()
    print("\nDemonstrating Stable Softmax:")
    corrected_softmax_issues()
    print("\nDemonstrating Log-Softmax:")
    log_sm_out = corrected_log_softmax_issues()
    print("\nConverting Log-Softmax Output Back to Probabilities:")
    print(log_softmax_to_probabilities(log_sm_out))
