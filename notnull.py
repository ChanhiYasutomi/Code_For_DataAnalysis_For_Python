# notnull(x) は、Pandasのデータフレームやシリーズ内の要素が欠損値でないかどうかを確認するための関数です。具体的な例を示します：

import pandas as pd
import numpy as np

# サンプルのデータフレームを作成
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, np.nan, 5],
}

df = pd.DataFrame(data)

# 'A' 列の各要素が欠損値でないか確認
not_null_A = df['A'].notnull() #反対はisnull()

print("Column 'A':")
print(not_null_A)

# サンプルのデータフレーム df を作成し、'A' 列と 'B' 列に数値および欠損値（NaN）が含まれています。
# df['A'].notnull() を使用して、'A' 列の各要素が欠損値でないかどうかを確認し、結果を not_null_A として保存します。
# 結果を表示します。not_null_A はブール型のシリーズで、各要素が欠損値でない場合は True、欠損値の場合は False となります。
# 出力結果は以下のようになります：

# Column 'A':
# 0     True
# 1     True
# 2    False
# 3     True
# 4     True
# Name: A, dtype: bool

# この結果から、'A' 列の各要素が欠損値でない場合は True が表示され、欠損値の場合は False が表示されます。notnull() 関数を使用することで、データフレームやシリーズ内の欠損値をフィルタリングしたり、条件に基づいた操作を行ったりすることができます。
