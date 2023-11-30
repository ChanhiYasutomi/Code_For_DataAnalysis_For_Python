# np.concatenate は、NumPyの関数で、複数の配列を結合する際に使用されます。
# 以下に、Pythonの具体例を挙げて np.concatenate の使用方法を説明します。
import numpy as np

# サンプルデータの作成
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
array3 = np.array([7, 8, 9])

# 1次元配列の結合
concatenated_array = np.concatenate([array1, array2, array3])
display("1次元配列の結合:\n", concatenated_array)

# 出力:
# 1次元配列の結合:
# [1 2 3 4 5 6 7 8 9]

# 2次元配列の作成
matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6]])

matrix2 = np.array([[7, 8, 9],
                    [10, 11, 12]])

# 列方向（縦方向）に結合
concatenated_matrix_rows = np.concatenate([matrix1, matrix2], axis=0)
display("\n列方向に結合:\n", concatenated_matrix_rows)

# 出力:
# 行方向に結合:
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]

# 行方向（横方向）に結合
concatenated_matrix_columns = np.concatenate([matrix1, matrix2], axis=1)
display("\n行方向に結合:\n", concatenated_matrix_columns)

# 出力:
# 列方向に結合:
# [[ 1  2  3  7  8  9]
#  [ 4  5  6 10 11 12]]

# この例では、np.concatenate を使用して1次元および2次元の配列を結合しています。
# axis パラメータを使用して、結合の方向（行または列）を指定することができます。
# なお、axis パラメータはデフォルトで0（行方向）です。
