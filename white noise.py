# 以下はPythonでホワイトノイズを生成し、その特性を示す具体例です。この例では、NumPyライブラリを使用しています。
import numpy as np
import matplotlib.pyplot as plt

# ホワイトノイズの生成
np.random.seed(0)
n = 100  # サンプル数
white_noise = np.random.normal(0, 1, n)  # 平均0、標準偏差1の正規分布に従うホワイトノイズ

# ホワイトノイズのプロット
plt.figure(figsize=(10, 4))
plt.plot(white_noise)
plt.title('White Noise')
plt.xlabel('Time')
plt.ylabel('Value')
plt.grid(True)
plt.show()

# このコードでは、np.random.normal(0, 1, n)によって、平均が0、標準偏差が1の正規分布に従うランダムなデータが生成されます。
# これがホワイトノイズです。生成されたホワイトノイズをプロットすることで、ランダム性、平均値0、一様な分散、無相関性などの特性が視覚化されます。
# ホワイトノイズは、実験データやシミュレーションの背景ノイズ、統計モデルの誤差項など、さまざまな分野で使用されます。
