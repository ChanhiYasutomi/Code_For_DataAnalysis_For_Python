import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# サンプルのDataFrameを作成
data = {'price': np.random.normal(0, 1, 1000)}  # 平均0、標準偏差1の正規分布からランダムなデータを生成

df = pd.DataFrame(data)

# ヒストグラムをプロット
plt.figure(figsize=(12, 8))  # 図のサイズを設定
sns.displot(df['price'], kde=True)  # 'price' 列の分布を可視化（kde=Trueでカーネル密度推定も表示）
plt.show()  # プロットを表示

# このコードは、SeabornとMatplotlibを使用して、サンプルのDataFrame内の 'price' 列の分布を可視化するものです。以下にコードの詳細を説明します：
# サンプルのDataFrameを作成します。このDataFrameには、平均0と標準偏差1の正規分布からランダムなデータが 'price' 列に格納されています。このデータはランダムに生成されています。
# plt.figure(figsize=(12, 8)) は、Matplotlibを使用して図（プロット）のサイズを設定するコードです。具体的には、図の幅を12インチ、高さを8インチに設定しています。これにより、プロットのサイズが大きくなります。
# sns.displot(df['price'], kde=True) はSeabornを使用してヒストグラムを作成し、カーネル密度推定も表示するコードです。df['price'] は 'price' 列のデータを指定しています。kde=True は、カーネル密度推定を有効にしています。カーネル密度推定は、データの分布を滑らかな曲線で表現し、データの確率密度関数を推定します。
# plt.show() は、作成したプロットを表示します。この行がないと、プロットは表示されません。

# コードを実行すると、 'price' 列のデータのヒストグラムが表示され、カーネル密度推定も上にオーバーレイ表示されます。これにより、データの分布が視覚化され、データポイントの集中度や中心傾向を把握できます。プロットのサイズが設定されているため、大きなプロットが表示されます。



# 対数変換ver
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# サンプルのDataFrameを作成
data = {'price': np.random.normal(0, 1, 1000)}  # 平均0、標準偏差1の正規分布からランダムなデータを生成

df = pd.DataFrame(data)

# ヒストグラムをプロット
plt.figure(figsize=(12, 8))  # 図のサイズを設定
sns.displot(np.log1p(df['price']), kde=True)  # 'price' 列の分布を可視化（kde=Trueでカーネル密度推定も表示）
plt.show()  # プロットを表示

# 提供されたコードは、SeabornとMatplotlibを使用して、サンプルのDataFrame内の 'price' 列の分布を可視化しています。しかし、このコードにはいくつかの変更が加えられています。具体的な説明は以下の通りです：
# サンプルのDataFrameを作成し、 'price' 列に平均0と標準偏差1の正規分布からランダムなデータを生成しました。
# plt.figure(figsize=(12, 8)) で図のサイズを設定し、図の幅を12インチ、高さを8インチに設定しています。これにより、プロットのサイズが大きくなります。
# sns.displot(np.log1p(df['price']), kde=True) は、Seabornを使用してヒストグラムを作成し、カーネル密度推定も表示するコードです。df['price'] 列のデータに対して np.log1p 関数を適用しています。
# np.log1p はデータの対数変換を行います。対数変換は、データが正の値で歪度が大きい場合に使用され、分布を対数スケールに変換します。kde=True はカーネル密度推定を有効にしています。
# 最後に、plt.show() でプロットを表示します。

# このコードを実行すると、'price' 列のデータが対数スケールでプロットされ、対数正規分布に近い形状を持つことが視覚化されます。このような変換は、特にデータが歪んでいる場合や外れ値の影響を軽減するために使用されます。
