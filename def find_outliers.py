import pandas as pd

def find_outliers(column):
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

# データセットを作成
data = {'Value': [10, 15, 20, 25, 30, 100, 105, 110, 115, 120, 600, 600]}
df = pd.DataFrame(data)

# find_outliers 関数を適用して 'Value' 列の外れ値と割合を検出
outliers, percentage = find_outliers(df['Value'])

# 外れ値を表示
display("外れ値:", outliers)

# 外れ値の割合を表示
display("外れ値の割合:", percentage)
