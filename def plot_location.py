# このコードは、Matplotlibを使用して散布図をプロットする関数 plot_location を定義し、それを呼び出している例です。具体的な例を以下に示します。

# 位置情報を可視化
# plt.scatterメソッドを使って、位置情報を可視化します。
# 引数については、xに経度、yに緯度、axisに表示範囲をタプル型の経緯度を指定します。

import pandas as pd

# サンプルのデータフレームを作成
data = {
    'pickup_longitude': [-74.05, -73.90, -73.80, -73.95, -73.78, -73.85, -73.92, -74.00, -73.88, -73.77],
    'pickup_latitude': [40.70, 40.75, 40.80, 40.65, 40.85, 40.68, 40.73, 40.78, 40.81, 40.79]
}
df_location = pd.DataFrame(data)

# 散布図をプロットする関数
def plot_location(x, y, axis):
    plt.scatter(x, y, s=1.0, alpha=0.5)
    plt.axis(axis)

# プロット領域のサイズを設定
plt.figure(figsize=(5, 5))

# plot_location関数を呼び出し、散布図をプロット
plot_location(df_location['pickup_longitude'], df_location['pickup_latitude'], 
              axis=[-74.1, -73.7, 40.6, 40.9])

# プロットを表示
plt.show()

# このコードの説明:
# サンプルの位置データを持つデータフレーム df_location を作成します。
# plot_location 関数は、x座標とy座標のデータを受け取り、指定された軸範囲で散布図をプロットします。s パラメータはプロットされる点のサイズ、alpha パラメータは点の透明度を設定します。
# plt.figure(figsize=(10, 10)) はプロット領域のサイズを設定しています。この場合、正方形のプロット領域が10x10インチで作成されます。
# plot_location 関数を呼び出して、pickup_longitude と pickup_latitude のデータを指定し、軸の範囲も指定しています。
# 最後に plt.show() を呼び出して、プロットを表示します。

# これにより、指定された座標データを含む散布図が表示されます。
