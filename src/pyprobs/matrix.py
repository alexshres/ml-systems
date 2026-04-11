"""
@file: matrix.py
@author: Alex Shrestha

Building a 2D matrix classusing a flat Python list as the underlying storage --- no NumPy.  Implementing just the basics:

Let A = Matrix(rows, cols, data)

* __getitem__ -> allows A[i, j]
* __setitem__ -> allows A[i, j] = x
* __matmul__  -> allows A @ B
"""


class Matrix:
    def __init__(self, rows: int, cols: int, data: list[float]):
        """
        Parameters
        ----------
        rows: int
            Number of rows in data 
        cols: int
            Number of cols in data
        data: list[float]
            Data in shape of one long list
        """

        if len(data) != rows * cols:
            raise ValueError("Length of data must equal rows * columns")

        self.rows = rows
        self.cols = cols
        self.data = data 

    def __getitem__(self, idx) -> list[float] | float:
        """
        Returns element of data if idx is a tuple, an entire row otherwise.

        Parameters
        ----------
        idx: tuple | int
            Tuple (i, j)
            Int i
        
        Returns
        -------
        list[float] | float:

        """
        if isinstance(idx, tuple):
            # grab row (i), col (j)
            i, j = idx

            if i >= self.rows:
                raise ValueError("i is out of bounds")
            if j >= self.cols:
                raise ValueError("j is out of bounds")

            return self.data[i*self.cols + j]
        else:
            return self.data[idx*self.cols:(idx+1)*self.cols]

    def __setitem__(self, indices: tuple[int, int], value: float):
        """
        Sets element of data based on indices

        Parameters
        ----------
        indices: tuple[int, int]
            Indices in data to set new value
        value: float
            Value that will replace current element
        """

        if not isinstance(indices, tuple):
            raise ValueError("Indices must be a tuple")

        i, j = indices

        if i >= self.rows:
            raise ValueError("i is out of bounds")
        if j >= self.cols:
            raise ValueError("j is out of bounds")

        self.data[i*self.cols + j] = value

    def transpose(self) -> "Matrix":
        """
        Returns
        -------
        Transpose of Matrix as a new object.
        """
        rows = self.cols
        cols = self.rows

        data_T = [0.] * (rows * cols)

        for i in range(rows):
            for j in range(cols):
                data_T[i*cols + j] = self.data[j*self.cols + i]

        return Matrix(rows, cols, data_T)

    def __matmul__(self, other: "Matrix") -> "Matrix":
        """
        Matrix multiplication given that the shapes match. Output is based on 
        self @ other.

        Parameters
        ----------
        other: Matrix
            Other matrix to multiply with current one

        Returns
        -------
        Matrix:
            Matrix object that is self @ other
        """

        if self.cols != other.rows:
            raise ValueError(f"Shape mismatch {self.cols} != {other.rows}")

        f_rows = self.rows
        f_cols = other.cols

        result = [0.] * (f_rows * f_cols)

        for i in range(f_rows):
            for j in range(f_cols):
                for k in range(self.cols):
                    self_value = self.data[i*self.cols + k]
                    other_value = other.data[k*other.cols + j]
                    result[i*f_cols + j] += self_value * other_value

        return Matrix(f_rows, f_cols, result)

if __name__ == "__main__":
    data1 = [[1.,0., 2.],[2., 1., 0.]]
    data1_flattened = [1., 0., 2., 2., 1., 0.]

    rows1 = 2
    cols1 = 3

    data2 = [[1.,0.,], [1., 2.],[0., 1.]]
    data2_flattened = [1., 0., 1., 2., 0., 1.]

    rows2 = 3
    cols2 = 2


    mat1 = Matrix(rows1, cols1, data1_flattened)
    mat1_T = mat1.transpose()

    mat2 = Matrix(rows2, cols2, data2_flattened)

    print(f"{mat1[0, 0]=}")
    print(f"{mat1[1]=}")
    print(f"{mat1_T.data=}")


    print(f"{(mat1 @ mat2).data}")

        
