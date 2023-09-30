# idxminは、PandasライブラリのSeriesオブジェクトやDataFrameの列に対して使用できる関数で、最小値を持つ要素のインデックス（行番号や列名）を返します。以下に具体例を挙げて説明します。
# まず、以下のDataFrameを考えます：
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'Salary': [50000, 60000, 45000, 52000]}

df = pd.DataFrame(data)

# このDataFrameにおいて、Salary列で最小の値を持つ行のインデックス（行番号）を取得したい場合、idxminを使用できます。

min_salary_index = df['Salary'].idxmin()
print(min_salary_index)

# このコードは、Salary列で最小の値を持つ行のインデックスである2を出力します。したがって、Charlieの行が最低の給与を持っていることがわかります。
# また、idxminをSeriesオブジェクトにも適用できます。以下は、数値のリストをSeriesに変換し、最小値を持つ要素のインデックスを取得する例です：
data = [10, 20, 15, 5, 25]
s = pd.Series(data)

min_index = s.idxmin()
print(min_index)

# このコードは、最小値を持つ要素のインデックスである3を出力します。したがって、元のリストの中で5が最小の値であることがわかります。
