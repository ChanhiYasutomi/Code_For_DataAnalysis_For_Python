import pandas as pd
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

def find_outliers(df):
    outliers_rate_dict = {}

    for column_name in df.columns:
        column = df[column_name]

        # 数値型の列でない場合はスキップ
        if not pd.api.types.is_numeric_dtype(column):
            print(f"列 '{column_name}' は数値型でないためスキップされます。")
            continue

        # データの平均値と標準偏差を計算
        mean = column.mean()
        std = column.std()

        # 外れ値の閾値を設定
        threshold = 2  # この値を調整して外れ値の基準を変更

        # 外れ値を検出する条件を設定
        lower_bound = mean - threshold * std
        upper_bound = mean + threshold * std

        # 外れ値を検出
        outliers = (column < lower_bound) | (column > upper_bound)

        # 外れ値の割合を算出
        outliers_rate = outliers.sum() / len(column)

        # 結果を辞書に保存
        outliers_rate_dict[column_name] = outliers_rate

    return outliers_rate_dict

# 処理①
data_inspection = pd.DataFrame({
    'Column Name': df.columns,
    'Data Type': df.dtypes,
    'Number of rows ': len(df),
    'Number of uniques ': df.nunique(),
    'Non-Null Count': df.count().values,
    'Null Count': df.isnull().sum(),
    'Null rate': (df.isnull().sum() / len(df)), #.round(5): 小数点5桁
    'date min': df['Date'].min(),
    'date max': df['Date'].max()
})

# 処理②
description = df.describe().T.reset_index().rename(columns={'index': 'Column Name'})
median = df.median(numeric_only=True).reset_index().rename(columns={'index': 'Column Name', 0: 'median'})

# 各カラムの最頻値を計算
mode_values = df.mode(numeric_only=True).iloc[0]

# 最頻値の割合を計算
mode_ratios = {}
for column in df.columns:
    if pd.api.types.is_numeric_dtype(df[column]):
        mode_value = mode_values[column]
        mode_ratio = (df[column] == mode_value).sum() / len(df)
        mode_ratios[column] = mode_ratio

# 最頻値とその割合をデータフレームに変換
mode = mode_values.reset_index().rename(columns={'index': 'Column Name', 0: 'mode'})
mode['rate mode'] = mode['Column Name'].map(mode_ratios)

# 処理②_別ver
# mean = df.mean(numeric_only=True).reset_index().rename(columns={'index': 'Column Name', 0: 'mean'})
# median = df.median(numeric_only=True).reset_index().rename(columns={'index': 'Column Name', 0: 'median'})

# # 各カラムの最頻値を計算
# mode_values = df.mode(numeric_only=True).iloc[0]

# # 最頻値の割合を計算
# mode_ratios = {}
# for column in df.columns:
#     if pd.api.types.is_numeric_dtype(df[column]):
#         mode_value = mode_values[column]
#         mode_ratio = (df[column] == mode_value).sum() / len(df)
#         mode_ratios[column] = mode_ratio

# # 最頻値とその割合をデータフレームに変換
# mode = mode_values.reset_index().rename(columns={'index': 'Column Name', 0: 'mode'})
# mode['rate mode'] = mode['Column Name'].map(mode_ratios)

# # mode = df.mode(numeric_only=True).iloc[0].reset_index().rename(columns={'index': 'Column Name', 0: 'mode'})
# # rate_mode = (df.mode(numeric_only=True).iloc[0] / len(df)).reset_index().rename(columns={'index': 'Column Name', 0: 'rate_mode'})

# std = df.std(numeric_only=True).reset_index().rename(columns={'index': 'Column Name', 0: 'std'})
# min = df.min(numeric_only=True).reset_index().rename(columns={'index': 'Column Name', 0: 'min'})
# quantile_25 = df.quantile(0.25, numeric_only=True).reset_index().rename(columns={'index': 'Column Name', 0.25: 'quantile_25'})
# quantile_50 = df.quantile(0.50, numeric_only=True).reset_index().rename(columns={'index': 'Column Name', 0.5: 'quantile_50'})
# quantile_75 = df.quantile(0.75, numeric_only=True).reset_index().rename(columns={'index': 'Column Name', 0.75: 'quantile_75'})
# max = df.max(numeric_only=True).reset_index().rename(columns={'index': 'Column Name', 0: 'max'})

# 処理③
data_inspection = pd.merge(data_inspection, description, how = 'left', on = 'Column Name')
data_inspection = pd.merge(data_inspection, mode, how = 'left', on = 'Column Name')

outliers_rate = find_outliers(df)
outliers_rate = pd.DataFrame(list(outliers_rate.items()), columns=['Column Name', 'outliers_rate']).reset_index(drop=True)
data_inspection = pd.merge(data_inspection, outliers_rate, how = 'left', on = 'Column Name')

# 処理③_別ver
# data_inspection = pd.merge(data_inspection, mean, how = 'left', on = 'Column Name')
# data_inspection = pd.merge(data_inspection, median, how = 'left', on = 'Column Name')
# data_inspection = pd.merge(data_inspection, mode, how = 'left', on = 'Column Name')
# data_inspection = pd.merge(data_inspection, std, how = 'left', on = 'Column Name')
# data_inspection = pd.merge(data_inspection, min, how = 'left', on = 'Column Name')
# data_inspection = pd.merge(data_inspection, quantile_25, how = 'left', on = 'Column Name')
# data_inspection = pd.merge(data_inspection, quantile_50, how = 'left', on = 'Column Name')
# data_inspection = pd.merge(data_inspection, quantile_75, how = 'left', on = 'Column Name')
# data_inspection = pd.merge(data_inspection, max, how = 'left', on = 'Column Name')

# outliers_rate = find_outliers(df)
# outliers_rate = pd.DataFrame(list(outliers_rate.items()), columns=['Column Name', 'outliers_rate']).reset_index(drop=True)
# data_inspection = pd.merge(data_inspection, outliers_rate, how = 'left', on = 'Column Name')
# data_inspection

# 処理④
data_inspection_else = pd.DataFrame({
    'Column Name': df.columns,
    'flag or not': df.apply(unique_to_binary),
    'columns details': None,
    'remarks': None,
    'trigger': None,
    'data exmaple': df.head(1).T[0] # or df.dropna().T.iloc[0]
})

data_inspection = pd.merge(data_inspection, data_inspection_else, how = 'left', on = 'Column Name')

data_inspection.to_csv('data_inspection.csv', index = 'false')
