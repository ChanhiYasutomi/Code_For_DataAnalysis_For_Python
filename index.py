# .index は、Pandasデータフレームやシリーズオブジェクトの属性の一つで、そのオブジェクトのインデックス（行ラベル）を取得するために使用されます。以下は具体的な例を示します。

import pandas as pd

# サンプルのデータフレームを作成
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 22, 35]
}

df = pd.DataFrame(data)

# データフレームのインデックスを取得
index = df.index

# このコードでは、以下のことが行われています：
# サンプルのデータフレーム df を作成します。このデータフレームには2つの列 'Name' と 'Age' が含まれています。
# df.index を使用して、データフレームのインデックス（行ラベル）を取得します。
# インデックスを表示して確認します。
# 出力結果は次のようになります：

RangeIndex(start=0, stop=4, step=1)

# この結果では、データフレーム df のインデックスが範囲インデックス (RangeIndex) であることが示されています。
# 範囲インデックスは、通常の数値インデックスであり、0から始まり、4未満で1ずつ増加します。
# データフレームやシリーズのインデックスは、データへのアクセスや操作に役立ちます。
