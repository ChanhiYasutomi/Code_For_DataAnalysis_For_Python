# .equals() メソッドは、2つの Pandas オブジェクトが同じ値を持つかどうかを比較するためのメソッドです。具体的な例を挙げて説明します。
import pandas as pd

# サンプルのデータフレームを作成
data1 = {'Name': ['Alice', 'Bob', 'Charlie'],
         'Age': [25, 30, 35],
         'Salary': [50000, 60000, 75000]}
df1 = pd.DataFrame(data1)

# 別のデータフレームを作成（同じデータ）
data2 = {'Name': ['Alice', 'Bob', 'Charlie'],
         'Age': [25, 30, 35],
         'Salary': [50000, 60000, 75000]}
df2 = pd.DataFrame(data2)

# 別のデータフレームを作成（データが異なる）
data3 = {'Name': ['Alice', 'Bob', 'Charlie'],
         'Age': [25, 30, 35],
         'Salary': [50000, 60000, 80000]}
df3 = pd.DataFrame(data3)

# df1とdf2を比較
result1 = df1.equals(df2)

# df1とdf3を比較
result2 = df1.equals(df3)

print("Result 1 (df1 equals df2):", result1)  # True
print("Result 2 (df1 equals df3):", result2)  # False

# この例では、df1 と df2 は同じデータを持っているため、.equals() を使って比較すると True が返ります。
# 一方で、df1 と df3 は "Salary" 列のデータが異なるため、.equals() を使って比較すると False が返ります。

# このメソッドは、データフレームやシリーズが同じ値を持っているかどうかを効率的に確認するために使用されます。
