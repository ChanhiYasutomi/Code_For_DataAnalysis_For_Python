# データ検品
# 以下は任意で追加する
# データセット名, 定義書有無
# 数値、日付、文字列、カテゴリとかでフォーマットは統一する -> これはmap処理する

# カラムごとにユニークな値が0または1であるかを確認し、1または0を付与
def unique_to_binary(column):
    unique_values = column.unique()
    if len(unique_values) == 2 and set(unique_values) == {0, 1}:
        return 1
    else:
        return 0

#外れ値割合(プラスマイナス5σ)
# # 各数値カラムの外れ値割合を計算
# def outlier_percentage(column):
#     mean = column.mean()
#     std = column.std()
#     lower_bound = mean - 5 * std
#     upper_bound = mean + 5 * std
#     outliers = (column < lower_bound) | (column > upper_bound)
#     outlier_percentage = outliers.sum() / len(column)
#     return outlier_percentage

# データ検品
data_inspection = pd.DataFrame({
    'Column Name': df.columns,
    'Data Type': df.dtypes.values,
    'Number of rows ': len(df),
    'Number of uniques ': df.nunique(),
    'Non-Null Count': df.count().values,
    'Null Count': df.isnull().sum(),
    'Null rate': (df.isnull().sum() / len(df)), #.round(5): 小数点5桁
    'date min': df['年月日'].min(),
    'date max': df['年月日'].max(),

    'mean': df.mean(numeric_only=True),
    'median': df.median(numeric_only=True),
    'mode': df.mode(numeric_only=True).iloc[0],
    'mode rate': (df.mode(numeric_only=True).iloc[0] / len(df)), #.round(5)
    'std': df.std(numeric_only=True),
    'min': df.min(numeric_only=True),
    '25 percentile': df.quantile(0.25, numeric_only=True),
    '50 percentile': df.quantile(0.50, numeric_only=True),
    '75 percentile': df.quantile(0.75, numeric_only=True),
    'max': df.max(numeric_only=True),

    'flag or not': df.apply(unique_to_binary),
    'columns details': None,
    'remarks': None,
    'trigger': None,
    'data exmaple': df.head(1).T[0] # or df.dropna().T.iloc[0]
}).reset_index()

display(data_inspection)

提供されたコードに基づいて、データセットの検査および情報収集のためのフレームワークが設定されています。これにより、データセットの品質を評価し、データの特性に関する洞察を得るのに役立つ情報が収集されます。以下は提供されたコードの詳細な説明です：
unique_to_binary 関数: この関数は、各カラムに対してユニークな値が0または1であるかどうかを確認し、その結果をフラグとして返します。これにより、カラムごとにバイナリフラグを設定することができます。たとえば、特定のカラムに2つのユニークな値（0と1）しか含まれない場合、そのカラムに対するフラグが1に設定されます。
コメントアウトされた outlier_percentage 関数: この関数は、各数値カラムに対して外れ値の割合を計算するために使用できるものです。外れ値は、平均から5標準偏差以上離れた値として定義されます。この関数を復活させてカスタマイズすることで、外れ値の評価が可能になります。
info_df データフレーム: このデータフレームは、データセットの各カラムに関する情報を整理しています。データの型、行数、ユニークな値の数、欠損値の数、平均、中央値、標準偏差、最小値、最大値などの統計情報が収集されています。
また、unique_to_binary 関数を適用して、各カラムに対するユニークな値が0または1であるかどうかのフラグも含まれています。
その他の列: コード内でコメントアウトされた列（'columns details'、'remarks'、'trigger'）は、データセットに関する追加情報を記録するためのものと思われます。必要に応じてこれらの列に情報を追加して、データセットに関する文書化を行うことができます。
このコードを使用することで、データセットの品質評価とデータの理解が行え、データ分析や前処理の準備に役立ちます。データセットに特有の要件に従って情報を追加し、データセットの検査プロセスをカスタマイズすることができます。
