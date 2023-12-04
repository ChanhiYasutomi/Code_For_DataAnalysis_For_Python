np.sortは、NumPyライブラリを使用して配列をソートするための関数です。以下に、np.sortの具体的な例を示します。
import numpy as np

# 1次元配列の例
arr_1d = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
sorted_arr_1d = np.sort(arr_1d)

print("Original 1D array:", arr_1d)
print("Sorted 1D array:", sorted_arr_1d)
# この例では、arr_1dという1次元のNumPy配列を作成し、np.sortを使用して昇順にソートしています。出力は次のようになります：

# Original 1D array: [3 1 4 1 5 9 2 6 5 3 5]
# Sorted 1D array: [1 1 2 3 3 4 5 5 5 6 9]

# 同様に、2次元配列や多次元配列にもnp.sortを適用することができます：
# 2次元配列の例
arr_2d = np.array([[3, 1, 4], [1, 5, 9], [2, 6, 5]])
sorted_arr_2d = np.sort(arr_2d, axis=None)  # axis=Noneは全体を対象にソート

print("Original 2D array:\n", arr_2d)
print("Sorted 2D array:", sorted_arr_2d)
# この場合、axis=Noneを指定することで、2次元の配列を1次元に平坦化してソートしています。出力は次のようになります：

# Original 2D array:
#  [[3 1 4]
#   [1 5 9]
#   [2 6 5]]
# Sorted 2D array: [1 1 2 3 4 5 5 6 9]

# これらの例から分かるように、np.sortはデフォルトで昇順にソートします。降順にソートしたい場合は、[::-1]を使って逆順に並べ替えることができます。
