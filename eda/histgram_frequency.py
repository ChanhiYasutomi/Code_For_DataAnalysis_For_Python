# 各カラムに対して処理を実行
for column in df.columns:
    # ヒストグラムを描画し、ビンの境界と度数を取得
    counts, bins, _ = plt.hist(df[column], bins=20, color='skyblue', edgecolor='black', density=False)

    # 相対度数、累積度数、相対累積度数を計算
    relative_freq = counts / sum(counts)
    cumulative_freq = counts.cumsum()
    relative_cumulative_freq = cumulative_freq / sum(counts)

    # ビンの境界と各度数をデータフレームに変換
    histogram_data = pd.DataFrame({
        'Bin_Start': bins[:-1],
        'Bin_End': bins[1:],
        'Frequency': counts,
        'Relative_Frequency': relative_freq,
        'Cumulative_Frequency': cumulative_freq,
        'Relative_Cumulative_Frequency': relative_cumulative_freq
    })

    # グラフにタイトルやラベルを追加（任意）
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')

    # データフレームを表示
    display(histogram_data)

    # グラフを表示
    plt.show()



# 以下は、具体的なデータとしてランダムに生成されたサンプルデータを用いて、各カラムに対するヒストグラムと相対度数、累積度数、相対累積度数を計算し、データフレームに格納して表示する例です。
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# サンプルデータの生成
np.random.seed(42)
data = {
    'Fresh': np.random.normal(0, 1, 1000),
    'Milk': np.random.normal(5, 2, 1000),
    'Grocery': np.random.normal(10, 3, 1000),
    'Frozen': np.random.normal(-3, 1, 1000),
    'Detergents_Paper': np.random.normal(8, 2, 1000),
    'Delicassen': np.random.normal(2, 1, 1000)
}

df = pd.DataFrame(data)

# 各カラムに対して処理を実行
for column in df.columns:
    # ヒストグラムを描画し、ビンの境界と度数を取得
    counts, bins, _ = plt.hist(df[column], bins=20, color='skyblue', edgecolor='black', density=False)

    # 相対度数、累積度数、相対累積度数を計算
    relative_freq = counts / sum(counts)
    cumulative_freq = counts.cumsum()
    relative_cumulative_freq = cumulative_freq / sum(counts)

    # ビンの境界と各度数をデータフレームに変換
    histogram_data = pd.DataFrame({
        'Bin_Start': bins[:-1],
        'Bin_End': bins[1:],
        'Frequency': counts,
        'Relative_Frequency': relative_freq,
        'Cumulative_Frequency': cumulative_freq,
        'Relative_Cumulative_Frequency': relative_cumulative_freq
    })

    # グラフにタイトルやラベルを追加（任意）
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')

    # データフレームを表示
    display(histogram_data)

    # グラフを表示
    plt.show()
  
# この例では、6つのカラム（'Fresh', 'Milk', 'Grocery', 'Frozen', 'Detergents_Paper', 'Delicassen'）に対して、ヒストグラムと相対度数、累積度数、相対累積度数を計算しています。
# データは正規分布から生成されているため、ヒストグラムは正規分布に近い形状になります。
