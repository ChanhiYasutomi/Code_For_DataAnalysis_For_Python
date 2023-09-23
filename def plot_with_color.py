# このコードは、matplotlibを使用して、経度（pickup_longitude）と緯度（pickup_latitude）に基づいて散布図をプロットするものです。
# また、各点の色とサイズをfare_amountに基づいて設定しています。以下は具体例を説明するコードです：

import pandas as pd
import matplotlib.pyplot as plt

# サンプルのデータフレームを作成
data = {
    'pickup_longitude': [-74.05, -73.90, -73.80, -73.95, -73.78, -73.85, -73.92, -74.00, -73.88, -73.77],
    'pickup_latitude': [40.70, 40.75, 40.80, 40.65, 40.85, 40.68, 40.73, 40.78, 40.81, 40.79],
    'fare_amount': [10, 20, 15, 25, 12, 18, 22, 8, 14, 16]
}
df_location = pd.DataFrame(data)

# 散布図をプロットする関数
def plot_with_color(x, y, data, axis=None):
    plt.scatter(x, y, s=data, c=data, cmap=plt.get_cmap('jet'), alpha=0.3)
    plt.axis(axis)
    plt.colorbar()
    plt.xlabel('longitude', fontsize=15)
    plt.ylabel('latitude', fontsize=15)

# プロット領域のサイズを設定
plt.figure(figsize=(5, 5))

# plot_with_color関数を呼び出し、散布図をプロット
plot_with_color(x=df_location['pickup_longitude'], 
                y=df_location['pickup_latitude'],
                data=df_location['fare_amount'],
                axis=[-74.1, -73.7, 40.6, 40.9])

# プロットを表示
plt.show()

# このコードでは、plot_with_color関数が経度と緯度をxとyとして受け取り、fare_amountの値を点のサイズと色として設定しています。
# 散布図のカラーマップは'jet'を使用しています。このように、点のサイズと色を変更することで、異なる情報を可視化できます。
