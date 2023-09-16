def get_vector_map(df, column):
    dim = df[column].nunique()
    elem = df[column].unique()

    vector_map = dict()

    for id, e in enumerate(elem):
        init = [0 for _ in range(dim)]
        init[id] = 1
        vector_map[e] = init

    return vector_map, dim  # 関数内にreturn文を配置

# このコードは、DataFrame内の一意のカテゴリカルな要素（列）をベクトルにマッピングする関数 get_vector_map を定義しています。以下に、この関数の具体的な説明と例を示します。

import pandas as pd

# サンプルのDataFrameを作成
data = {
    'Category': ['A', 'B', 'C', 'A', 'B', 'C'],
}

df = pd.DataFrame(data)

# カテゴリカル列 'Category' をベクトルにマッピングする関数
def get_vector_map(df, column):
    dim = df[column].nunique()  # 列内の一意の要素数を取得
    elem = df[column].unique()  # 列内の一意の要素を取得

    vector_map = dict()

    for id, e in enumerate(elem):
        init = [0 for _ in range(dim)]  # ゼロで初期化されたリストを生成
        init[id] = 1  # インデックスがidの要素を1に設定
        vector_map[e] = init

    return vector_map, dim

# カテゴリカル列 'Category' をベクトルにマッピング
vector_map, dim = get_vector_map(df, 'Category')

# 結果を表示
print("ベクトルマップ:")
for category, vector in vector_map.items():
    print(f"{category}: {vector}")

print(f"次元数: {dim}")

# このコードでは、以下の手順で関数 get_vector_map を実行しています：
# dim 変数には、指定されたカラム（'Category'）内の一意の要素数が格納されます。この場合、'A'、'B'、'C' の3つの一意の要素があるため、dim は3になります。
# elem 変数には、指定されたカラム内の一意の要素（'A'、'B'、'C'）が格納されます。
# vector_map は、要素（'A'、'B'、'C'）を対応するベクトルにマッピングするための空の辞書です。ループを使用して、各要素をベクトルに変換し、vector_map に格納します。
# 各要素は、指定されたカラム内での順序に基づいて、対応するインデックスが1で、他のインデックスが0のリストで表されます。
# vector_map と dim の値が関数から返され、結果が表示されます。
# この関数は、カテゴリカルなデータをベクトル形式に変換する際に便利です。例えば、機械学習モデルにカテゴリカルデータを供給する際に使用できます。
