# サイズ指定
fig, ax = plt.subplots(figsize=(15, 8))

# 色の設定
flatui = ["#9b59b6", "#3498db"]
sns.set_palette(flatui)

# 年齢
col = 'age'

# カーネル密度推定を2群で表示
sns.kdeplot(data=df_pred_1, x=col, hue="target", fill=True, alpha=0.1)
plt.show()

# このPythonコードは、Seabornライブラリを使用してカーネル密度推定プロットを作成し、2つの異なるクラス（またはカテゴリ）間で年齢（age）の分布を比較するものです。以下にコードの各部分を説明します：
# fig, ax = plt.subplots(figsize=(15, 8)): 新しいMatplotlibの図（figure）と軸（axis）を作成し、図のサイズを15x8インチに設定します。
# flatui = ["#9b59b6", "#3498db"]: グラフの色を定義します。ここでは2つの色（紫と青）をリストで指定しています。
# sns.set_palette(flatui): Seabornのプロットスタイルに指定した色パレット（flatui）を設定します。
# col = 'age': 分析したいカラム（特徴）の名前を指定します。この場合、年齢（age）カラムを分析対象としています。

# sns.kdeplot(data=df_pred_1, x=col, hue="target", fill=True, alpha=0.1): Seabornのkdeplot関数を使用してカーネル密度推定プロットを作成します。以下のパラメータを指定しています：
# data=df_pred_1: データフレーム df_pred_1 を指定しています。
# x=col: x軸に使用するカラム名を col で指定しています（ここでは年齢）。
# hue="target": カテゴリ別に異なる色で表示するカラム名を target で指定しています。これにより、2つのクラス（またはカテゴリ）で分布を比較できます。
# fill=True: カーネル密度プロットを塗りつぶすオプションです。Trueに設定すると、プロットが塗りつぶされます。
# alpha=0.1: プロットの透明度を設定します。この場合、プロットは透明度が低いため、データの重なりがわかりやすくなります。
# plt.show(): プロットを表示します。

# このコードは、2つの異なるカテゴリ（target）に属するデータポイントの年齢分布を比較するために使用されます。密度推定プロットを通じて、2つのカテゴリの分布がどのように異なるかを視覚的に理解できます。また、fill=Trueおよびalphaを使用してプロットを見やすくし、データの重なりを視覚化しています。

# このデータフレームには、2つのカテゴリ（"target"列の値が0または1）と年齢（"age"列）が含まれています。

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'age': [25, 28, 32, 22, 30, 29, 35, 36, 27, 24, 40, 41],
    'target': [0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)
# このデータを使用して、2つの異なるカテゴリ（target=0およびtarget=1）に属するデータポイントの年齢分布を比較するカーネル密度推定プロットを作成するPythonコードを示します。
# サイズ指定
fig, ax = plt.subplots(figsize=(10, 6))

# 色の設定
flatui = ["#9b59b6", "#3498db"]
sns.set_palette(flatui)

# 年齢
col = 'age'

# カーネル密度推定を2群で表示
sns.kdeplot(data=df, x=col, hue="target", fill=True, alpha=0.1)
plt.show()

# このコードは、Seabornライブラリを使用してカーネル密度推定プロットを作成します。プロットには、2つのカテゴリ（target=0およびtarget=1）のデータポイントの年齢分布が表示されます。
密度プロットは透明度が低く、データの重なりがわかりやすくなっています。このプロットを通じて、2つのカテゴリの年齢分布の違いを視覚的に比較できます。
