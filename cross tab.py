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
