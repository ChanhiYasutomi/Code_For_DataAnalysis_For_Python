# plt.pie を使用して円グラフを描画するコードの具体例を説明します。この例では、success_rate というデータを元に円グラフを作成します。
import matplotlib.pyplot as plt

# サンプルのデータ (success_rate) を作成
success_rate = {'Success': 75, 'Failure': 25}

# 円グラフを描画
plt.pie(success_rate.values(),  # 各カテゴリの値を指定
        labels=success_rate.keys(),  # 各カテゴリのラベルを指定
        startangle=90,  # 開始角度を90度に設定（12時の方向から開始）
        autopct='%.0f%%',  # カテゴリの割合をパーセント表示
        textprops={'fontsize': 20},  # ラベルのフォントサイズを指定
        counterclock=False)  # 時計回りにカテゴリを配置

# グラフのタイトルを設定
plt.title('Success Rate')

# グラフを表示
plt.show()

# このコードの説明：
# import matplotlib.pyplot as plt で Matplotlib ライブラリをインポートします。
# success_rate は、{'Success': 75, 'Failure': 25} というデータです。これは2つのカテゴリ 'Success' と 'Failure' の成功率を表しています。

# plt.pie を使用して円グラフを描画します。以下のパラメータが使用されています:
# success_rate.values(): 各カテゴリの値を指定します。
# labels=success_rate.keys(): 各カテゴリのラベルを指定します。
# startangle=90: 円グラフの開始角度を90度に設定します。これにより、12時の方向から開始します。
# autopct='%.0f%%': カテゴリの割合をパーセント表示します。小数点以下0桁のパーセント表示を行います。
# textprops={'fontsize': 20}: ラベルのフォントサイズを20に設定します。
# counterclock=False: 時計回りにカテゴリを配置します。
# plt.title('Success Rate') でグラフにタイトルを設定します。

# 最後に plt.show() を使用してグラフを表示します。

# これにより、成功率を示す円グラフが描画され、各カテゴリの割合がパーセント表示されます。
