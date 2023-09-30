import pandas as pd

def find_outliers(column):
    # 数値型の列でない場合、エラーメッセージを表示して処理を中止
    if not pd.api.types.is_numeric_dtype(column):
        raise ValueError("列は数値型である必要があります。")

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
    return outliers, outliers_rate
    # return outliers_rate #, outliers # こうしたら割合を算出できる。

# データセットを作成
data = {'A': [1, 2, 3, 4, 5, 1000], 'B': ["a", "a", "a", "a", "a", "a"]}
df = pd.DataFrame(data)

# find_outliers 関数を適用して 'A' 列の外れ値と割合を検出
outliers, percentage = find_outliers(df['A']) #これは正常に処理される
# outliers, percentage = find_outliers(df['B']) #これは数値方じゃないからエラーが出る(raise ValueError("列は数値型である必要があります。"))

# 外れ値を表示
display("外れ値:", outliers)

# 外れ値の割合を表示
display("外れ値の割合:", percentage)
