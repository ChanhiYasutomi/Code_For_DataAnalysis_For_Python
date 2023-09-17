# .strftime('%A') は、Pythonの datetime オブジェクトまたはPandasの日時列を文字列にフォーマットするためのメソッドです。特に、'%A' は曜日をフルスペル（例：Monday、Tuesday）で表示するためのフォーマット指定です。以下に具体的な例を示します：

import datetime

# datetimeオブジェクトを作成
date = datetime.datetime(2023, 9, 15)  # 2023年9月15日 (例として金曜日)

# 曜日をフルスペルで表示
day_of_week = date.strftime('%A')

print(day_of_week)  # 出力: Friday
この例では、datetime.datetime を使用して2023年9月15日の日付を表す date オブジェクトを作成し、.strftime('%A') を使用してその日付から曜日情報を取得しています。

# Pandasを使用した場合も同様に、日時列から曜日情報を抽出できます。以下はPandasを使用した例です：

import pandas as pd

# サンプルのデータフレームを作成
data = {
    'purchase_date': ['2023-09-15', '2023-09-16', '2023-09-17'],
}

df = pd.DataFrame(data)

# 日付文字列を日時列に変換
df['purchase_date'] = pd.to_datetime(df['purchase_date'])

# 曜日をフルスペルで表示
df['day_of_week'] = df['purchase_date'].dt.strftime('%A')

print(df)
# この例では、Pandasのデータフレームに日時列を持つデータを読み込み、.dt.strftime('%A') を使用して各日時の曜日情報を新しい列として追加しています。結果として、各購買日に対する曜日情報が表示されます。
