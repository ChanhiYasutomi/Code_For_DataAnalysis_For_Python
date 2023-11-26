# pd.qcut()は、データを指定された数の分位点（quantile）で等分し、各分位点にラベルを付けるためのPandasの関数です。
# この関数は主に連続したデータを離散的な区間に分割するために使用されます。
# 以下は、pd.qcut()の具体例です:
import pandas as pd
import numpy as np

# サンプルデータ生成
data = pd.DataFrame({'Values': np.random.rand(100) * 100})

# pd.qcutを使用してデータを10分割し、それぞれの区間にラベルを付ける
data['Decile_interval'] = pd.qcut(data['Values'], q=10) # 浮動小数点での区間で表示される
data['Decile_int'] = pd.qcut(data['Values'], q=10, labels=False) # 整数で表示される
data['Decile_labels'] = pd.qcut(data['Values'], q=10, labels=['A','B','C','D','E','F','G','H','I','J']) # ラベル(labels = ['x',...)が表示される

# 結果を表示
display(data.head())

# この例では、np.random.rand(100) * 100で生成された0から100までの乱数を持つデータフレームがあります。
# pd.qcut()を使用して、このデータを10等分し、それぞれの区間に0から9までのラベルを付けています。 q引数は分位点の数を指定します。
# なお、labels=Falseとすることでラベルを数値で表示しています。labels引数を指定することで、カスタムのラベルを使用することもできます。
