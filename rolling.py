import pandas as pd

# サンプルのデータを作成
data = {'価格': [10, 15, 20, 18, 25, 30, 28, 35, 40]}
df = pd.DataFrame(data)

# 移動平均を計算するためのウィンドウを指定
window_size = 3

# 移動平均を計算
rolling_mean = df['価格'].rolling(window=window_size).mean() #3日間移動平均
rolling_min_periods_mean = df['価格'].rolling(window=window_size,min_periods=1).mean() #3日間移動平均(min_periods込み)

# 結果を新しい列としてデータフレームに追加
df['移動平均'] = rolling_mean
df['移動平均_min_periods'] = rolling_min_periods_mean

# 結果を表示
display(df)

# このPythonコードは、Pandasライブラリを使用して、与えられたデータフレームに対して移動平均を計算し、結果を新しい列としてデータフレームに追加する方法を示しています。
# 最初に、サンプルのデータフレーム df を作成します。このデータフレームには、価格データが含まれています。
# 移動平均を計算するために、rolling() メソッドを使用します。rolling() メソッドは、移動平均を計算するためのウィンドウサイズを指定することができます。この例では、ウィンドウサイズを3日間に設定しました。
# rolling_mean 変数に、df['価格'].rolling(window=window_size).mean() を代入しています。これにより、'価格' 列の3日間移動平均が計算されます。
# 同様に、rolling_min_periods_mean 変数に、df['価格'].rolling(window=window_size,min_periods=1).mean() を代入しています。この場合、min_periods パラメータが使用されており、初日からの平均値が計算されます。つまり、観測数が3未満の場合でも移動平均が計算されます。
# 計算した移動平均を、新しい列 '移動平均' および '移動平均_min_periods' として、元のデータフレーム df に追加します。
# 最終的に、計算結果を表示します。データフレームには、元の価格データに加えて、2つの異なる移動平均が含まれています。
# このようにして、Pandasを使用してデータフレームに移動平均を追加する方法が示されています。
