# plt.text は Matplotlib ライブラリを用いてグラフ上にテキストを追加するための関数です。具体例を挙げて説明します。
import matplotlib.pyplot as plt

# サンプルデータの作成
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# 折れ線グラフの描画
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Data')

# グラフにテキストを追加
plt.text(3, 20, 'Max Value', fontsize=12, color='red')

# グラフの装飾
plt.title('Sample Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)

# グラフを表示
plt.show()

# この例では、plt.text を使用して、グラフ上の座標 (3, 20) に 'Max Value' というテキストを追加しています。
# 引数には、テキストを表示する x 座標、y 座標、テキストの内容、フォントサイズ、色などを指定します。これにより、グラフ上に注釈や重要な情報を追加することができます。
