filter() は、Pandasデータフレームに対して特定の条件に基づいて列をフィルタリングするための関数です。具体的な例を示します：
import pandas as pd

# サンプルのデータフレームを作成
data = {
    'Person_Name': ['Alice', 'Bob', 'Charlie'],
    'Person_Age': [25, 30, 35],
    'Company_Name': ['ABC Inc.', 'XYZ Corp.', 'LMN Ltd.'],
    'Company_Revenue': [100000, 80000, 120000]
}

df = pd.DataFrame(data)

# 列名が 'Person_' で始まる列をフィルタリング
filtered_df = df.filter(like='Person_', axis=1)

print("Filtered DataFrame:")
print(filtered_df)

# このコードでは、以下のことが行われています：
# サンプルのデータフレーム df を作成し、'Person_Name'、'Person_Age'、'Company_Name'、'Company_Revenue' 列が含まれています。
# df.filter(like='Person_', axis=1) を使用して、列名が 'Person_' で始まる列をフィルタリングします。like パラメータは列名に対する部分一致検索を行い、axis=1 は列方向を指定します。
# フィルタリングされた結果を filtered_df として保存し、表示します。
# 出力結果は以下のようになります：

# Filtered DataFrame:
#   Person_Name  Person_Age
# 0       Alice          25
# 1         Bob          30
# 2     Charlie          35

# 結果として、列名が 'Person_' で始まる列 ('Person_Name' と 'Person_Age') が抽出され、新しいデータフレーム filtered_df に格納されています。このように、filter() 関数を使用して、特定の列名パターンに一致する列を取得することができます。
