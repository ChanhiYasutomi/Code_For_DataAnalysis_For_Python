# 提供されたコードは、Pandasを使用して、Unixエポック時間（通常は秒単位の整数）から日付と時刻の情報を持つPythonのdatetimeオブジェクトに変換し、その後タイムゾーンを調整して日付情報だけを取得する方法を示しています。
# 以下に具体的な例を示します。
# まず、サンプルデータを作成します。このデータはUnixエポック時間（秒）で日付と時刻を表します。
import pandas as pd

data = {'time': [1634121600, 1634208000, 1634294400]}
df = pd.DataFrame(data)

# 次に、提供されたコードを適用して、Unixエポック時間をdatetimeオブジェクトに変換し、タイムゾーンを調整して日付情報だけを取得します。
from datetime import datetime, timedelta

# Unixエポック時間をdatetimeオブジェクトに変換し、タイムゾーンを調整して日付情報だけを取得
df['time'] = df['time'].apply(lambda x: datetime.fromtimestamp(x) + timedelta(hours=9)).dt.date

# このコードでは、次のことが行われています：
# .apply(lambda x: ...) メソッドを使用して、各行の 'time' 列の値に対して関数を適用します。
# 関数内では、datetime.fromtimestamp(x) を使用してUnixエポック時間をdatetimeオブジェクトに変換し、.dt.date を使用して日付情報だけを取得します。
# タイムゾーンの調整として timedelta(hours=9) を追加しています。これにより、通常のUTCからUTC+9（日本のタイムゾーン）に調整されます。
# 変換後のデータフレームは、日付情報だけを含む新しい 'time' 列を持つことになります。結果は以下のようになります：

#   dateoftransactionconfirm
# 0                2021-10-14
# 1                2021-10-15
# 2                2021-10-16

# これにより、Unixエポック時間から正確な日付情報が抽出され、タイムゾーンが調整されたデータフレームが得られます。
