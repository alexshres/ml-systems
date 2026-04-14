"""

@file: prefix_sum.py

Implements Blelloch's  Up-Sweep/Down-Sweep Prefix Sum Algorithm

There are two phases:
1. Collect Phase (Up-Sweep)
2. Distribute Phase (Down-Sweep)

Collect Phase:

* [1, 2, 3, 4]
* [1, 3, 3, 7]
* [1, 3, 3, 10]

Distribute Phase:
* [1, 3, 3, 0]
* [1, 0, 3, 3]
* [0, 1, 3, 6]
* [1, 3, 6, 10]
"""

import math


def up_sweep(arr: list) -> list:
    """
    Parameters
    ----------
    arr: list
        List to have exclusive prefix sum performed

    Returns
    -------
    list
        Up sweeped version of the array
    """

    result = arr.copy()
    n = len(result)

    # assuming n is a power of 2 and we have that many processors
    # for loop will "simulate" what each processor is doing
    procs = math.log2(n)

    for d in range(int(procs)):
        skip = int(math.pow(2, d+1))
        for k in range(0, n, skip):
            result[k+skip-1] = result[k + (skip//2)-1] + result[k + (skip//2)]

    return result

def down_sweep(arr: list) -> list:
    n = len(arr)
    procs = int(math.log2(n))

    for d in range(procs):
        skip = int(math.pow(2, d+1))

        for k in range(0, n, skip):
            arr[k+skip-1] = arr[k+(skip//2)-1] + arr[k+(skip//2)]


    return arr


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    print(f"{arr=}")
    up_sweep_result = up_sweep(arr)

    print(f"{up_sweep_result=}")

    down_sweep_result = down_sweep(up_sweep_result)

    print(f"{down_sweep_result=}")
