# Pandasのデータフレーム列から特定の時間部分を抽出するには、dtアクセサを使用します。strftimeメソッドはPythonのdatetimeオブジェクトに対して使われることが一般的で、Pandasのデータフレーム列には直接適用できません。以下は、データフレーム列から時間部分（hour）を抽出する方法です。

import pandas as pd

# 仮のデータフレームを作成
data = {'dateofpurchase_jst': ['2023-09-19 10:15:30', '2023-09-19 14:30:45', '2023-09-19 18:45:15']}
df_before_groupby = pd.DataFrame(data)

# 日時列をDatetime型に変換
df_before_groupby['dateofpurchase_jst'] = pd.to_datetime(df_before_groupby['dateofpurchase_jst'])

# 時間部分（hour）を抽出
df_before_groupby['hour'] = df_before_groupby['dateofpurchase_jst'].dt.hour

display(df_before_groupby)
# このコードは、dateofpurchase_jst 列を datetime オブジェクトに変換し、dt.hour を使用して時間部分（hour）を新しい列 hour に抽出しています。データフレームの各行には、時間部分が含まれた新しい列が追加されます。

# 結果は次のようになります：

#     dateofpurchase_jst  hour
# 0  2023-09-19 10:15:30    10
# 1  2023-09-19 14:30:45    14
# 2  2023-09-19 18:45:15    18
# これにより、日時列から時間部分を抽出できます。必要に応じて、strftimeメソッドを使用して時間部分の書式をカスタマイズすることもできます。
