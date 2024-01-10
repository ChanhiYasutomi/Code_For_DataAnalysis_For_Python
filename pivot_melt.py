# pivotとunpivotは、データ操作において重要な概念で、主に表形式のデータを変形するために使用されます。
# これらの操作は、主にデータベースやデータ分析のコンテキストで使われます。
# 以下に、PythonのPandasライブラリを使用してpivotとunpivotの具体的な例を示します。

# Pivotの例:
# Pivotは、行と列を入れ替え、新しい表を作成します。以下は、Pandasを使用した簡単な例です。
import pandas as pd

# サンプルデータを作成
data = {'Date': ['2022-01-01', '2022-01-01', '2022-01-02', '2022-01-02'],
        'Variable': ['A', 'B', 'A', 'B'],
        'Value': [10, 20, 15, 25]}

df = pd.DataFrame(data)
display(df)

# Pivotを行う
pivot_df = df.pivot(index='Date', columns='Variable', values='Value').reset_index()
display(pivot_df)

# この例では、元のデータフレームdfに対して、Dateを行インデックス、Variableを列名、Valueを値として持つ新しいデータフレームが作成されます。

# Unpivotの例:
# Unpivotは、逆に行と列を入れ替えて、新しい表を作成します。以下は、Pandasを使用した例です。

# Unpivotを行う
unpivot_df = pd.melt(pivot_df, id_vars='Date', var_name='Variable', value_name='Value')
display(unpivot_df)

# pivotとmelt（unpivot）は、データの形状を変更する強力なツールであり、特にデータの集計や可視化などで便利です。
# データの特定の要約や可視化のためには、データが適切な形に整形されていることが重要です。
