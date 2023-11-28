# np.random.choice([1, 0], size=100)は、指定されたリスト [1, 0]からサンプリングして、サイズが100の配列を生成するNumPyの関数です。
# これは二項分布（Binomial Distribution）を模倣するもので、各試行が1または0である場合を考えることができます。
# 具体的な例として、以下は np.random.choice を使用して二項分布に従うデータを生成するコードです：

import numpy as np
import matplotlib.pyplot as plt

# 二項分布からサンプリング
data = np.random.choice([1, 0], size=100)

# 生成されたデータの表示
print(data)

# ヒストグラムのプロット
plt.hist(data, bins=[-0.5, 0.5, 1.5], align='mid', color='skyblue', edgecolor='black')
plt.title('Histogram of Binomial Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# この例では、np.random.choice([1, 0], size=100)で [1, 0]からサンプリングして、サイズが100の二項分布に従うデータを生成しています。
# 生成されたデータは1または0のいずれかの値であり、ヒストグラムで可視化されています。
