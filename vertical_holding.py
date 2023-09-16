# PythonのPandasライブラリを使用して、DataFrameの形式をワイドフォーマットからロングフォーマットに変換する操作を行っています。以下、コードの詳細な説明です。
import pandas as pd

data = {
    'ID': [1, 2, 3],
    'M1': [100, 200, 300],
    'M2': [150, 250, 350]
}

df = pd.DataFrame(data)

# id_vars=['ID']：'ID' 列を識別子変数として残すことを指定しています。
# value_vars=['M1', 'M2']：変形（展開）する列を指定しています。これらの列は 'Metric' と 'Value' として新しい列に変換されます。
# var_name='Metric'：新しい変数名を設定し、これに 'M1' と 'M2' の名前が適用されます。
# value_name='Value'：新しい値の列の名前を設定し、元々の 'M1' と 'M2' の値が 'Value' として変換されます。

melted_df = pd.melt(df, id_vars=['ID'], value_vars=['M1', 'M2'], var_name='Metric', value_name='Value')
