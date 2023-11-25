# cumprod()メソッドは、累積積（cumulative product）を計算するために使用されます。各要素が前の要素との積の累積を計算し、結果として新しいシリーズまたはデータフレームを生成します。
# 以下に、cumprod()メソッドの具体的な例を示します：

import pandas as pd

# サンプルデータの作成
data = {'Value': [2, 3, 4, 5]}
df = pd.DataFrame(data)

# 'Value'列の累積積を計算
df['Cumulative Product'] = df['Value'].cumprod()

print(df)

# # このコードでは、'Value'列の各要素に対してcumprod()メソッドを使用し、新しい列 'Cumulative Product' に累積積が計算されます。結果は以下のようになります：
#    Value  Cumulative Product
# 0      2                   2
# 1      3                   6
# 2      4                  24
# 3      5                 120
# 各行の 'Cumulative Product' 列の値は、それまでの行の 'Value' 列の値の積の累積を表しています。
