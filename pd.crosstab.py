# クロス集計
pd.crosstab(dataframe['columns'], dataframe['columns']).reset_index()

# pd.crosstab(dataframe['columns_1'], dataframe['columns_2'], dataframe['columns'_3]).reset_index()のようにカラムが3つある場合に、
# dataframe['columns_1']かつdataframe['columns_2']の条件(行)でdataframe['columns'_3](列)のクロス集計になる。
# dataframe['columns_1'] * dataframe['columns_2'] * dataframe['columns'_3]の条件でクロス集計される。

# pd.crosstab() 関数は、クロス集計（クロスタブ）を行うために使用されます。この関数は、2つ以上のカテゴリカルな変数（カラム）をクロス集計して、クロス集計表を作成します。以下に具体例を示します。
# 例として、あるウェブサイトのユーザーの性別（'Gender'）と購買履歴（'Purchased'）をクロス集計してみましょう。

import pandas as pd

# サンプルデータを作成
data = {
    'User': ['User1', 'User2', 'User3', 'User4', 'User5'],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
    'Purchased': [1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

# クロス集計を行う
cross_tab = pd.crosstab(df['Gender'], df['Purchased'], margins = True)

Purchased	0	1	All
Gender			
Female	  2	0	2
  Male	  0	3	3
  All	    2	3	5

# このコードでは、'Gender' カラム（性別）と 'Purchased' カラム（購買履歴）のデータをクロス集計しています。pd.crosstab() 関数により、性別（'Gender'）を行に、購買履歴（'Purchased'）を列に持つクロス集計表が作成されます。
# この表には、各セルに対応するクロス集計の値が表示されます。例えば、Male（男性）のユーザーのうち、1人が購入しており、Female（女性）のユーザーのうち、1人が購入していることがわかります。
# pd.crosstab() 関数では、さまざまなオプションが利用でき、集計関数（aggfunc）、合計行と列の表示（margins）、さらなる統計情報の計算などを行うことができます。

# pd.crosstab（クロスタブ）は、Pandasライブラリで提供されているクロス集計（Cross-Tabulation）を行うための便利なメソッドです。
# クロス集計は、2つ以上のカテゴリカル変数（カテゴリやカテゴリの組み合わせ）に基づいてデータを要約し、クロス集計テーブル（クロスタブ）として表示します。以下に、Pythonコードでpd.crosstabを具体的な例と共に説明します。
# 例として、あるウェブサイトのユーザーの性別と購買商品カテゴリに関するデータを考えてみましょう。データフレームには、ユーザーごとの性別と購買カテゴリが含まれています。

import pandas as pd

# サンプルのデータを作成
data = {
    'User': ['User1', 'User2', 'User3', 'User4', 'User5'],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Electronics', 'Clothing']
}

df = pd.DataFrame(data)

# このデータを使用して、pd.crosstabを使って性別と購買カテゴリのクロス集計を行います。
# クロス集計を実行
cross_tab = pd.crosstab(df['Gender'], df['Category'])

# 上記のコードでは、以下のことが行われています：
# pd.crosstab メソッドを呼び出し、次のパラメータを指定しています：
# df['Gender']: クロス集計の行になるカテゴリカル変数を指定します。ここでは性別 ('Gender') 列を指定しています。
# df['Category']: クロス集計の列になるカテゴリカル変数を指定します。ここでは購買カテゴリ ('Category') 列を指定しています。
# このコードを実行すると、性別と購買カテゴリに関するクロス集計テーブルが生成されます。出力は次のようになります：

# Category  Clothing  Electronics
# Gender                         
# Female           1            1
# Male             1            2

# このテーブルから、性別と購買カテゴリの組み合わせごとのユーザー数がわかります。
# たとえば、Female（女性）で Clothing（衣類）を購買したユーザーは1人、Male（男性）で Electronics（電子製品）を購買したユーザーは2人です。pd.crosstabを使用することで、カテゴリカルデータの関係を簡単に可視化および要約できます。



# pd.crosstabを使用してマルチインデックスを作成するには、indexパラメータにリストを渡すことで複数のカラムを指定できます。以下に具体的な例を示します。
import pandas as pd
import numpy as np

# サンプルデータの作成
data = {
    'R_score': ['A', 'B', 'A', 'B', 'A', 'B'],
    'F_score': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
    'M_score': ['High', 'Low', 'Medium', 'High', 'Low', 'Medium'],
    'Value': [10, 15, 20, 25, 30, 35]
}

df = pd.DataFrame(data)

# pd.crosstabを使用してマルチインデックスを作成
result = pd.crosstab(index=[df['R_score'], df['F_score']], columns=df['M_score'], values=df['Value'], aggfunc=np.sum)

# pd.crosstab([df['R_score'], df['F_score']], df['M_score'])
#    └ pd.crosstabを使用すると、デフォルトで各セルにカウントが入ります。

# R_scoreとF_scoreがインデックスとして使用され、M_scoreが列として使用されています。
# 各セルには対応する組み合わせの出現回数（カウント）が入ります。

display(result)

# この例では、R_scoreが1つ目のインデックス、F_scoreが2つ目のインデックスとして使用され、M_scoreが列として使用されています。各セルには対応する値の合計が入ります。
