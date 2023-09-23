# diff() は、Pandasのデータフレームやシリーズオブジェクトで使用できるメソッドで、要素間の差分を計算するために使用されます。具体的な例を示します。

import pandas as pd

# サンプルのデータフレームを作成
data = {
    'A': [10, 15, 22, 30],
    'B': [5, 12, 18, 25]
}

df = pd.DataFrame(data)

# データフレームの列 'A' の隣接する要素間の差分を計算
diff_A = df['A'].diff()
diff_B = df['B'].diff()

diff_A_2 = df['A'].diff(2)
diff_B_2 = df['B'].diff(2)

diff_A_minus = df['A'].diff(-1)
diff_B_minus = df['B'].diff(-1)

# データフレームに新しい列として差分を追加
df['Diff_A'] = diff_A
df['Diff_B'] = diff_B

df['Diff_A_2'] = diff_A_2
df['Diff_B_2'] = diff_B_2

df['Diff_A_minus'] = diff_A_minus
df['Diff_B_minus'] = diff_B_minus

# このコードでは、以下のことが行われています：
# サンプルのデータフレーム df を作成します。このデータフレームには2つの列 'A' と 'B' が含まれています。
# df['A'].diff() を使用して、'A' 列の隣接する要素間の差分を計算します。結果は新しいシリーズオブジェクト diff_A に格納されます。
# df データフレームに新しい列 'Diff_A' を追加し、差分データを格納します。
# 最終的に、データフレームを表示して、'A' 列の差分と 'Diff_A' 列の追加を確認します。

# 出力結果は次のようになります：

# index	A	B	Diff_A	Diff_B	Diff_A_2	Diff_B_2	Diff_A_minus	Diff_B_minus
# 0	10	5	NaN	NaN	NaN	NaN	-5.0	-7.0
# 1	15	12	5.0	7.0	NaN	NaN	-7.0	-6.0
# 2	22	18	7.0	6.0	12.0	13.0	-8.0	-7.0
# 3	30	25	8.0	7.0	15.0	13.0	NaN	NaN

# 'Diff_A' 列は 'A' 列の隣接する要素間の差分を示しており、最初の行では欠損値 (NaN) となっています。これは、最初の要素には前の要素が存在しないためです。差分の計算は、データの変化やトレンドの把握などの分析に役立ちます。
