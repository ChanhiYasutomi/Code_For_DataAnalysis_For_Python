# plt.figure(figsize=(10, 8)) の行は、Matplotlibを使用して図のサイズを設定するためのコードです。具体的には、幅を10インチ、高さを8インチに設定しています。これにより、後続の sns.heatmap 関数で生成されるヒートマップの図のサイズが指定されたサイズになります。

# sns.heatmap(df.corr(), annot=True, cmap='Blues') はSeabornライブラリを使用して、相関行列をヒートマップとして可視化するコードです。以下に具体的な例を示します：
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# サンプルのDataFrameを作成
data = {'A': np.random.rand(100),
        'B': np.random.rand(100),
        'C': np.random.rand(100)}

df = pd.DataFrame(data)

# 相関行列を計算
corr_matrix = df.corr()

# ヒートマップをプロット
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='Blues')
plt.show()

# このコードでは、サンプルのDataFrame df から相関行列を計算し、その相関行列を sns.heatmap でヒートマップとして可視化しています。
# corr_matrix = df.corr()：DataFrame df の相関行列を計算し、それを corr_matrix に格納します。

# sns.heatmap(corr_matrix, annot=True, cmap='Blues')：相関行列 corr_matrix をヒートマップとしてプロットします。annot=True は、各セルに相関係数の値を表示する注釈を有効にし、cmap='Blues' はカラーマップを 'Blues' に設定します。
# このコードを実行すると、数値列間の相関係数がヒートマップとして表示されます。ヒートマップは、相関が高い領域を濃い色で、相関が低い領域を淡い色で示します。注釈を有効にしているため、各セルに相関係数の値が表示されます。ヒートマップを使用すると、データセット内の数値列間の相関関係を視覚的に把握できます。




