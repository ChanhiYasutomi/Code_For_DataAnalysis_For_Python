# 四分位数を使った方法（四分位範囲の1.5倍以上離れているものを除外）
# このコードは、IQR（四分位範囲）を使用して外れ値を検出し、指定されたDataFrameから外れ値を取り除くカスタム関数 outlier_iqr を定義しています。以下に関数の詳細を説明します：
def outlier_iqr(df, columns=None):
    if columns == None:
        columns = df.columns

    for col in columns:
        q1 = df[col].describe()['25%']  # 1st Quartile (25th percentile)
        q3 = df[col].describe()['75%']  # 3rd Quartile (75th percentile)
        
        # 四分位範囲 (IQR) を計算
        iqr = q3 - q1 
        
        # 外れ値の範囲を計算
        outlier_min = q1 - iqr * 1.5
        outlier_max = q3 + iqr * 1.5

        # 範囲から外れている値を除く
        df = df[(df[col] >= outlier_min) & (df[col] <= outlier_max)]
        
    return df
  
# この関数は、以下の引数を受け取ります：
# df: 対象のDataFrame。
# columns（オプション）: 外れ値の検出を行う列のリスト。指定しない場合、DataFrameのすべての列が対象となります。

# 関数の主要なステップは次の通りです：
# 引数 columns が指定されない場合、すべての列が columns に設定されます。
# 指定された各列に対して、第1四分位数（25パーセンタイル）、第3四分位数（75パーセンタイル）を計算します。
# 四分位範囲（IQR）を計算し、これは第3四分位数から第1四分位数を引いた値です。
# 外れ値の範囲を計算し、外れ値を定義します。通常、IQRの1.5倍の範囲を外れ値の閾値として使用します。
# 各列に対して、外れ値の範囲外にある値を取り除きます。この操作により、外れ値が除外された新しいDataFrameが作成されます。
# 最終的に、処理が完了したDataFrameが返されます。
# この関数を使用すると、外れ値を検出してDataFrameから取り除くことができます。外れ値の定義や閾値を変更する場合、コード内の値を調整することができます。



# 提供された関数 outlier_iqr は、IQR（四分位範囲）を使用して外れ値を検出し、指定されたDataFrameから外れ値を削除するものです。以下に具体例を示します：
# まず、必要なライブラリをインポートします。
import pandas as pd
import numpy as np

# 次に、サンプルのDataFrameを作成します。
# サンプルのDataFrameを作成
data = {'A': [1, 2, 3, 4, 100],
        'B': [5, 6, 7, 8, 200],
        'C': [9, 10, 11, 12, 300]}

df = pd.DataFrame(data)
# このDataFrameには、外れ値として100、200、300という大きな値が含まれています。
# そして、outlier_iqr 関数を使用して外れ値を削除します。

# 外れ値を削除
filtered_df = outlier_iqr(df)

# 結果を表示
print(filtered_df)

# このコードを実行すると、outlier_iqr 関数が呼び出され、外れ値が含まれている列（A、B、C列）から外れ値が削除された新しいDataFrame filtered_df が作成されます。
# 結果は次のようになります：

#    A  B   C
# 0  1  5   9
# 1  2  6  10
# 2  3  7  11
# 3  4  8  12

# この結果からわかるように、関数 outlier_iqr は外れ値を削除し、外れ値を含む行がDataFrameから取り除かれています。
