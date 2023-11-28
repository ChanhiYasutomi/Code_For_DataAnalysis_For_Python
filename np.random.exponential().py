# np.random.exponential(size=100)は、指数分布（Exponential Distribution）に従う乱数を生成するNumPyの関数です。
# 指数分布は生存時間分析などでよく使用される確率分布で、特定の事象が発生するまでの時間の確率分布をモデル化します。
# 指数分布の確率密度関数は以下のように表されます:
# f(x;λ) = λe**λx

# ここで、λは尺度パラメータです。
# 具体的な例として、以下は指数分布から生成される乱数のヒストグラムをプロットするコードです:
import numpy as np
import matplotlib.pyplot as plt

# 指数分布から乱数生成
data = np.random.exponential(scale=1.0, size=100)

# ヒストグラムのプロット
plt.hist(data, bins = 30, density = True, alpha = 0.7, color = 'skyblue', edgecolor = 'black')
plt.title('Histogram of Exponential Distribution')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.show()

# この例では、np.random.exponential(scale=1.0, size=100)で尺度パラメータが1.0の指数分布から乱数を生成しています。
# 生成された乱数をヒストグラムで可視化しています。
