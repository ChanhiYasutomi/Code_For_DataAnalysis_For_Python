# Frequency Encoding（頻度エンコーディング）は、カテゴリカルなデータを数値データに変換するテクニックの一つです。各カテゴリの出現頻度を使用して、カテゴリを対応する数値にエンコードします。
# これにより、カテゴリごとの情報が数値データにキャプチャされ、機械学習モデルに適した形式に変換されます。
# 以下に、Pythonコードを使用してFrequency Encodingを説明する具体的な例を示します。

import pandas as pd

# サンプルデータを含むデータフレームを作成
data = {
    'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'A', 'C', 'B', 'B']
}

df = pd.DataFrame(data)

# カテゴリごとの出現頻度を計算
category_counts = df['Category'].value_counts().reset_index()
category_counts.columns = ['Category', 'Frequency']

# カテゴリを頻度に置き換える
df_encoded = df.merge(category_counts, on='Category', how='left')
df_encoded.drop(columns=['Category'], inplace=True)

print(df_encoded)

# このコードでは、次の手順を実行しています：
# カテゴリカルなデータを持つデータフレーム df を作成します。
# value_counts() メソッドを使用して、各カテゴリの出現頻度を計算します。それぞれのカテゴリの頻度が category_counts という新しいデータフレームに格納されます。
# merge() メソッドを使用して、元のデータフレーム df と category_counts を 'Category' カラムをキーにして結合します。これにより、カテゴリをその出現頻度に置き換えます。
# 最後に、'Category' カラムを削除して、Frequency Encodingが適用されたデータフレーム df_encoded を得ます。
# 上記のコードを実行すると、以下のようなデータフレーム df_encoded が得られます：

#    Frequency
# 0          4
# 1          4
# 2          4
# 3          2
# 4          4
# 5          4
# 6          4
# 7          2
# 8          4
# 9          4

# カテゴリ 'A' は4回、カテゴリ 'B' も4回、カテゴリ 'C' は2回出現しているため、それぞれのカテゴリが対応する頻度にエンコードされました。
# これにより、カテゴリカルな情報が数値データに変換され、機械学習モデルに適した形式になります。
