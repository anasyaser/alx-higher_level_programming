def square_matrix_simple(matrix=[]):
    nmatrix = matrix.copy()
    result = []
    for lst in matrix:
        cur_lst = []
        for num in lst:
            cur_lst.append(num ** 2)
        result.append(cur_lst)
    return result
