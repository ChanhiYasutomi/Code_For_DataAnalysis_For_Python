# (※要注意)
# 以下をId(ユニーク)と属性で分けている理由としてdataframe.groupby([['Id','attribute_1', 'attribute_2', 'attribute_3','attribute_n']])[columns].sum().reset_index()のようにgroubyをしたら、nullの部分が弾かれてグループ化され、母数が減少するため。
# そのためIdと属性を分割し、後にinner joinしている。
# 代替案として引数に dropna = False を設定すればいいかもしれないが確実かつ安全な処理では以下のようにした方がいい。
columns = ['2023-01', '2023-02', '2023-03', '2023-04', '2023-05', '2023-06', '2023-07', '2023-08', '2023-09', '2023-10', '2023-11', '2023-12']
only_id = dataframe.groupby(['Id'])[columns].sum().reset_index()　# nullがないことが前提(あるいは処理済み)
attribute = dataframe[['Id','attribute_1', 'attribute_2', 'attribute_3','attribute_n']].drop_duplicates()

dataframe = pd.merge(only_id, attribute, how = 'inner',left_on='Id',right_on='Id') # inner joinした理由はユニークであり、欠損がなかったから(確かnull処理はしていない。)


# Group by null どうなる？
# GROUP BY 節にリストした列において、NULL 値を含む各行は単一グループに属します。 つまり、すべての NULL 値がまとめてグループ化されます。
# これにより母数のレコード数が減る現象が起きる(※要注意)

# apply loop processing for selected columns
# 値が1以上であれば1を付与し、それ以外は0を付与する。
for column in columns:
    dataframe[columns] = dataframe[columns].apply(lambda x: 1 if x >= 1 else 0)

# 行方向にcolumnsの値をsumし、sum_visitに格納。
dataframe['sum_visit'] = dataframe[columns].sum(axis=1).astype(int)

# sum_visitに格納された値が数字の範囲であれば '~頻度'を付与してfrequencyに格納。
dataframe['frequency'] = dataframe['sum_visit'].apply(lambda row: '高頻度' if 5 <= row <= 7 else
                                                                  '中頻度' if 3 <= row <= 4 else
                                                                  '低頻度' if 1 <= row <= 2 else
                                                                  '未視聴')



import pandas as pd

# データをリストとして定義
data = [
    [1, 'Product A', '2023-01-05'],
    [1, 'Product A', '2023-02-10'],
    [1, 'Product A', '2023-03-15'],
    [2, 'Product B', '2023-03-24'],
    [2, 'Product A', '2023-03-27'],
    [2, 'Product A', '2023-03-30'],
    [3, 'Product C', '2023-01-01'],
    [3, 'Product C', '2023-02-20'],
]

# データフレームを生成
columns = ['customer_id', 'product_name_now', 'purchase_date']
data = pd.DataFrame(data, columns=columns)

# 'customer_id' でグループ化
grouped_data = data.groupby('customer_id')

# グループごとに情報を表示
for customer_id, group_data in grouped_data:
    display(f'Customer ID: {customer_id}')
    display(group_data)
    print('\n')

# 提供されたコードは、Pandasを使用してデータフレームを customer_id でグループ化し、各グループの情報を表示するものです。コードは正しい構造を持っており、次のことを行います：
# データをリストとして定義し、それを pd.DataFrame を使用してデータフレームに変換します。
# customer_id 列を基準にデータフレームをグループ化します。これにより、各 customer_id ごとにグループが形成されます。
# for ループを使用して、各グループごとに customer_id とそれに関連するデータを表示します。display 関数を使用して customer_id とグループ内のデータを表示し、print('\n') によって各グループの間に空行を挿入します。
# 提供されたデータとコードを使用すると、各 customer_id ごとに対応するデータが表示され、それぞれのグループの情報がわかります。データが正確に表示されることを確認できます。



import pandas as pd
import numpy as np

data = {
    'Category': ['Electronics', 'Books', None, 'Books', None],
    'Product': ['Laptop', 'None', 'Smartphone', 'Textbook', None],
    'Sales': [1000, 20, 800, 30, None]
}

df = pd.DataFrame(data)

# NaNを持つ行もグループに含めない
# こうなるとNoneの部分はdropnaされてしまいnullのデータが予期せず落とされる。
display(df.groupby('Category', as_index = False)["Sales"].sum())

print('\n')

# NaNを持つ行もグループに含める（dropna=False）
# dropna=Falseすることでnullで予期せずデータが落ちることはない。
display(df.groupby('Category', dropna=False, as_index = False)["Sales"].sum())
