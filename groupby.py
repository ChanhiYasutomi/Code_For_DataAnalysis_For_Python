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



# df.groupby('Category', as_index=False) における as_index=False は、Pandasの groupby 操作において、グループ化した列をインデックスにしないオプションを指定するためのパラメータです。
# デフォルトでは、groupby 操作を実行すると、指定した列（ここでは 'Category' 列）が新しいDataFrameのインデックスになります。つまり、グループ化した結果が新しいDataFrameの行インデックスになります。
# この動作は、一部の状況では便利ですが、データを操作する際にはインデックスになることが望ましくない場合もあります。
# as_index=False を指定すると、グループ化した結果のインデックスに指定した列を使用せず、0から始まる連番の整数インデックスが自動的に生成されます。つまり、グループ化されたデータが新しいDataFrameの列に含まれることになります。
# 以下は、as_index=False を使用した例です:
import pandas as pd

data = {'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
        'Value': [10, 20, 15, 15, 30, 40]}

df = pd.DataFrame(data)

# 'Category' 列でグループ化し、as_index=False を指定
result = df.groupby('Category', as_index=False).sum()

print(result)

# このコードは、'Category' 列でグループ化された各カテゴリーの合計値を計算し、新しいDataFrameを生成します。
# as_index=False を指定したため、グループ化されたカテゴリーが新しいDataFrameの列として保持されています。結果は次のようになります：
#   Category  Value
# 0        A     30
# 1        B     30
# 2        C     70
# このように、as_index=False を指定することで、グループ化結果が新しいDataFrameの列として保持され、インデックスにならないようになります。



# groupbyメソッドを使用することで、DataFrameを特定の列（ここでは'Gender'列）の値に基づいてグループに分け、その後に各グループに対して統計的な操作を行うことができます。
# 以下に一般的な例を示し、Pythonの具体的なコードで説明します。
# 仮想的なデータを用いて例を示します：
import pandas as pd

# 仮想的なデータを作成
data = pd.DataFrame({
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Age': [25, 30, 22, 35, 28, 32],
    'Salary': [50000, 60000, 45000, 70000, 55000, 80000]
})

# 'Gender'列を基準にグループ化
groupby_gender = data.groupby('Gender')

# 各グループに対して平均、中央値、データ数、合計を計算
mean_values = groupby_gender.mean()
median_values = groupby_gender.median()
count_values = groupby_gender.count()
sum_values = groupby_gender.sum()

# 結果を表示
display("Mean Values:")
display(mean_values)

display("\nMedian Values:")
display(median_values)

display("\nCount Values:")
display(count_values)

display("\nSum Values:")
display(sum_values)

# このコードでは、groupby_genderによって'Gender'列を基準にデータがグループ化されています。
# その後、各統計量（平均、中央値、データ数、合計）が計算されています。これにより、異なる性別に関連する統計情報が得られます。

# データフレームdataが以下のようになっていると仮定します：
#   Gender  Age  Salary
# 0   Male   25   50000
# 1 Female   30   60000
# 2   Male   22   45000
# 3 Female   35   70000
# 4   Male   28   55000
# 5 Female   32   80000
# 上記のコードを実行すると、各性別に対して平均、中央値、データ数、合計が計算され、それぞれの結果が表示されます。
