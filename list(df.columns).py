# このコードでは、Pandasを使用してCSVファイルからデータを読み込み、そのデータフレームの列名を表示します。

import pandas as pd

# サンプルデータを作成しCSVファイルに保存
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}

# サンプルデータをデータフレームに変換
df = pd.DataFrame(data)

# データフレームをCSVファイルに保存
df.to_csv('sample_data.csv', index=False)

# CSVファイルを読み込んでデータフレームを作成
filepath = 'sample_data.csv'
df = pd.read_csv(filepath)

# データフレームの列名を表示
columns = list(df.columns)
for col in columns:
    print(col)
  
# このコードでは、まずサンプルデータを含むデータフレームを作成し、それをCSVファイルに保存します。次に、pd.read_csv() を使用してCSVファイルを読み込み、データフレームを作成します。最後に、データフレームの列名を取得し、それらをループで一つずつ表示します。
# 実行すると、以下のような出力が得られます：

# Name
# Age
# City

# これは、データフレームの列名が表示されていることを示しています。
