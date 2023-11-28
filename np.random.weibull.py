# np.random.weibullは、Weibull分布からのランダムなサンプルを生成するNumPyの関数です。
# Weibull分布は確率変数が特定の形状パラメータと尺度パラメータに従う確率分布です。
# 以下は、np.random.weibullを使用してWeibull分布からサンプルを生成し、ヒストグラムで分布を可視化する例です。
import numpy as np
import matplotlib.pyplot as plt

# Weibull分布からランダムサンプル生成
data = np.random.weibull(1.5, 1000000)

# ヒストグラムで分布を可視化
plt.hist(data, bins=50, density=True, alpha=0.7, color='blue', edgecolor='black')
plt.title('Weibull Distribution')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.show()

# この例では、形状パラメータが1.5で、サンプル数が1000000のWeibull分布からのランダムサンプルを生成し、ヒストグラムで分布を可視化しています。 
# Weibull分布は形状パラメータによって異なる形状を持つため、異なる形状パラメータを試してみると分布の変化が観察できます。
