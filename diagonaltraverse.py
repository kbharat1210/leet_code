def findDiagonalOrder(mat):
    if not mat:
        return []

    m, n = len(mat), len(mat[0])
    result = []
    diagonal_dict = {}

    for i in range(m):
        for j in range(n):
            diagonal_sum = i + j
            if diagonal_sum not in diagonal_dict:
                diagonal_dict[diagonal_sum] = []
            diagonal_dict[diagonal_sum].append(mat[i][j])

    sorted_diagonals = sorted(diagonal_dict.items())
    for diagonal_sum, diagonal in sorted_diagonals:
        if diagonal_sum % 2 == 0:
            result.extend(diagonal)
        else:
            result.extend(diagonal[::-1])

    return result