#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    square_matrix = list()
    sq_row = list()
    for row in matrix:
        sq_row = []
        for i in row:
            sq_row.append(i * i)
        square_matrix.append(sq_row)
    return square_matrix
