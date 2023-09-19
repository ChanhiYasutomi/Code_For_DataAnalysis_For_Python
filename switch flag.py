# データをリストとして定義
data = [
    [1, 'Product A', '2023-01-05'],
    [1, 'Product A', '2023-02-10'],
    [1, 'Product A', '2023-03-15'],
    [1, 'Product A', '2023-03-18'],
    [1, 'Product A', '2023-03-21'],
    [1, 'Product B', '2023-03-24'],
    [1, 'Product A', '2023-03-27'],
    [1, 'Product A', '2023-03-30'],

    [2, 'Product C', '2023-01-01'],
    [2, 'Product C', '2023-02-20'],
    [2, 'Product D', '2023-02-23'],
    [2, 'Product C', '2023-03-01'],
    [2, 'Product C', '2023-03-05'],
    [2, 'Product C', '2023-03-08'],
    [2, 'Product C', '2023-03-11'],
    [2, 'Product D', '2023-03-14'],
]

# データフレームを生成
columns = ['customer_id', 'now_product_name', 'purchase_date']
data = pd.DataFrame(data, columns=columns)

data['before_product_name'] = data.groupby(['customer_id'])['product_name_now'].shift()
reset_index = data[data['before_product_name'].isnull()].index

# グループごとに最初の 'product_name_now' 値を取得し、欠損値を補完
for index in reset_index:
    customer_id = data.loc[index, 'customer_id']
    first_product_name = data[data['customer_id'] == customer_id]['product_name_now'].iloc[0]
    data.loc[index, 'before_product_name'] = first_product_name

data['switch flag'] = np.where(data['product_name_now'] != data['before_product_name'],1,0)

# このコードは、与えられたデータを使用して、顧客ごとに製品の変更が発生した場合にスイッチフラグを設定するためのPythonコードです。以下はこのコードのステップごとの説明です。
# 最初に、データをリストとして定義し、それをdata変数に格納します。このデータは、各行が顧客ID、現在の製品名、および購入日を含むリストで構成されています。

# 次に、pandasライブラリを使用して、データをデータフレームに変換します。データフレームの列は、customer_id（顧客ID）、now_product_name（現在の製品名）、およびpurchase_date（購入日）です。
# before_product_name列を作成し、それをグループごとに現在の製品名の前の製品名に設定します。これは、groupbyとshiftメソッドを使用して実現されます。shiftメソッドは、指定された列の値を指定した行数だけシフトするために使用され、ここでは前の製品名を取得します。before_product_name列は、前の製品名を含みます。
# reset_index変数には、before_product_name列が欠損値である行のインデックスが含まれます。これらの行は各顧客の最初の購入を表します。
# グループごとに、最初の購入の製品名を取得し、それを欠損値がある行に設定します。これにより、最初の購入時にbefore_product_name列が正しく補完されます。

# 最後に、switch flag列を作成し、np.where関数を使用して、現在の製品名と前の製品名が異なる場合に1、同じ場合に0を設定します。これにより、製品の変更が発生したかどうかを示すスイッチフラグが作成されます。

# このコードを実行すると、データフレームにbefore_product_name列とswitch flag列が追加され、各顧客の購入ごとに製品の変更がどのように発生したかが示されます。
