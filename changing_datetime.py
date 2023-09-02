# Timestamp__c 列を datetime 型に変換(JST変換)
dataframe['columns_timestamp'] = pd.to_datetime(dataframe['columns_timestamp']) + pd.Timedelta(hours=9)

#日付抽出
dataframe['date'] = dataframe['columns_timestamp'].apply(lambda x: x.date())

# example below
# pd.Timedelta(hours=9)は、PythonのPandasライブラリを使用して作成される時間の差を表すオブジェクトです。具体的には、このコードは「9時間」を表現しています。
# PandasのTimedeltaオブジェクトは、時間の差や経過時間を表現するために使用されます。Timedeltaオブジェクトは、日数、時間、分、秒、ミリ秒、マイクロ秒、ナノ秒などの単位で時間の差を表すことができます。
# 例えば、pd.Timedelta(hours=9)は、9時間の時間差を表します。このオブジェクトを使うことで、時間を加算、減算、またはデータフレームの列に時間を追加するなどの操作が可能になります。

# 以下はいくつかの例です：
import pandas as pd

# 9時間を表すTimedeltaオブジェクトの作成
time_difference = pd.Timedelta(hours=9)

# 時間の加算
new_time = pd.Timestamp('2023-09-02 12:00:00') + time_difference
print(new_time)  # 2023-09-03 21:00:00

# データフレームの列に時間の差を追加
df['経過時間'] = df['開始時刻'] + pd.Timedelta(hours=3)
# これらの例では、pd.Timedelta(hours=9)を使って9時間の時間差を表し、それを他の時間やデータフレームに適用しています。
