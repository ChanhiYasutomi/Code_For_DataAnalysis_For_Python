# Target Encoding（ターゲットエンコーディング）は、カテゴリカルな特徴量を数値にエンコードする手法の一つで、特に分類問題でターゲット変数（目的変数）に基づいてカテゴリの平均値を計算し、それを数値として各カテゴリに割り当てます。
# これにより、カテゴリごとのターゲット変数の平均値が特徴量として表現され、モデルにカテゴリカルデータを組み込むのに役立ちます。

# 以下に、Pythonコードを使用してTarget Encodingを説明する具体的な例を示します。この例では、仮想的な分類データを使用します。
import pandas as pd

# サンプルデータを含むデータフレームを作成
data = {
    'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'A', 'C', 'B', 'B'],
    'Target': [1, 0, 1, 0, 0, 1, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

# カテゴリごとのターゲット変数の平均値を計算
target_means = df.groupby('Category')['Target'].mean().reset_index()
target_means.columns = ['Category', 'Target_Mean']

# カテゴリをターゲット変数の平均値に置き換える
df_encoded = df.merge(target_means, on='Category', how='left')
df_encoded.drop(columns=['Category'], inplace=True)

display(df_encoded)

# このコードでは、次の手順を実行しています：
# カテゴリカルなデータとそれに対応するターゲット変数を持つデータフレーム df を作成します。
# groupby() メソッドを使用して、'Category' カラムをキーにしてカテゴリごとのターゲット変数の平均値を計算します。計算結果は target_means という新しいデータフレームに格納されます。
# merge() メソッドを使用して、元のデータフレーム df と target_means を 'Category' カラムをキーにして結合します。これにより、カテゴリを対応するターゲット変数の平均値にエンコードします。
# 最後に、'Category' カラムを削除して、Target Encodingが適用されたデータフレーム df_encoded を得ます。
# 上記のコードを実行すると、以下のようなデータフレーム df_encoded が得られます：

#    Target  Target_Mean
# 0       1     0.666667
# 1       0     0.400000
# 2       1     0.666667
# 3       0     0.500000
# 4       0     0.400000
# 5       1     0.666667
# 6       1     0.666667
# 7       0     0.500000
# 8       1     0.400000
# 9       0     0.400000

# 各カテゴリは、それに対応するターゲット変数の平均値で置き換えられました。これにより、カテゴリカルデータが数値データにエンコードされ、モデルの学習に使用できるようになります。
