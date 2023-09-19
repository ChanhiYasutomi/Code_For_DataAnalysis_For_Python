# np.timedelta64(1, 'Y') は、NumPyで使われる時間間隔を表現するオブジェクトです。このオブジェクトは、年単位の時間間隔を表現します。具体的には、1つの単位（年）を表現しています。

# 以下に具体例を示します。
import numpy as np

# 1年間の時間間隔を表現する timedelta64 オブジェクトを作成
one_year = np.timedelta64(1, 'Y')

# 例: 2年後の日付を計算する
current_date = np.datetime64('2023-09-15')
future_date = pd.to_datetime(current_date) + (2 * one_year)

# 出力したら '2025-09-14 11:38:24' が算出される
# この例では、np.timedelta64(1, 'Y') を使って1年間の時間間隔を表現し、それを使って現在の日付から2年後の日付を計算しています。計算結果は 2025-09-15 になります。
# このように、np.timedelta64(1, 'Y') は年単位の時間間隔を表現し、日付や時刻の計算に利用できます。

import pandas as pd
import numpy as np

# 仮想のDataFrameを作成
data = {'age_1': [np.datetime64('1990-01-15'), np.datetime64('1985-03-20'), np.datetime64('1998-11-05')]}
df_birth = pd.DataFrame(data)

# 'age_1' 列から年齢を計算して新しい列 'age' を追加
df_birth['age'] = ((pd.to_datetime('now') + pd.Timedelta(hours=9)) - df_birth['age_1']) / np.timedelta64(1, 'Y')
df_birth['age'] = df_birth['age'].astype(int)

# このコードは、PandasとNumPyを使用して、日付情報から年齢を計算し、整数値として新しい列 'age' に追加するものです。コードの詳細を説明します。
# 仮想のDataFrame df_birth を作成します。このDataFrameには 'age_1' 列が含まれており、日付情報（np.datetime64）が格納されています。

# 'age_1' 列から年齢を計算するために、'age' 列を新たに作成します。年齢の計算は以下のように行います：
# pd.to_datetime('now') は現在の日時を取得します。
# pd.Timedelta(hours=9) は日本の標準時（UTC+9）の時差を表します。これにより、日本の時刻で計算されます。
# ((pd.to_datetime('now') + pd.Timedelta(hours=9)) - df_birth['age_1']) は現在の日時から 'age_1' 列の各日付を引いて、経過した時間を計算します。
# / np.timedelta64(1, 'Y') は計算された時間差を年単位に変換します。'Y' は年を表します。
# 'age' 列のデータ型を整数型（int）に変換します。これにより、小数部分が切り捨てられ、年齢が整数値として格納されます。

# 結果として、DataFrame df_birth には 'age_1' 列と計算された 'age' 列が含まれています。この 'age' 列には各日付に対応する年齢が整数値として格納されています。
