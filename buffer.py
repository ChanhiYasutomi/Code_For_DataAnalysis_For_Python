import pandas as pd
from datetime import datetime, timedelta

data = {'date': [datetime(2023, 1, 1), datetime(2023, 1, 2), datetime(2023, 1, 3)],
        'value': [10, 20, 30]}

df = pd.DataFrame(data)

# バッファ 1日分を含む期間を設定
df_start = df.date.min() - timedelta(days=1)
df_end   = df.date.max() + timedelta(days=1)

print("データの最小日付:", df.date.min())
print("データの最大日付:", df.date.max())
print("バッファを含む期間の始まり:", df_start)
print("バッファを含む期間の終わり:", df_end)

# バッファを含めることで、データの期間を少し拡張し、境界条件や計算の安定性を向上させることができます。
# 特に、データ分析や時系列データの処理において、バッファの考慮は重要です。
