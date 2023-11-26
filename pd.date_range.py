# pd.date_rangeは、指定された範囲と頻度に基づいて日付のDatetimeIndexを生成するためのPandasの関数です。以下は具体的な例です。
import pandas as pd

# 2023年1月1日から7日後までの日付を1日ごとに生成
date_range_1 = pd.date_range(start='2023-01-01', periods=7, freq='D')
print("Date Range 1:")
print(date_range_1)

# 2023年1月1日から7日後までの日付を2日ごとに生成
date_range_2 = pd.date_range(start='2023-01-01', periods=4, freq='2D')
print("\nDate Range 2:")
print(date_range_2)

# 2023年1月1日から12月31日までの月初めの日付を生成
date_range_3 = pd.date_range(start='2023-01-01', end='2023-12-31', freq='MS')
print("\nDate Range 3:")
print(date_range_3)

# この例では、異なる頻度（1日ごと、2日ごと、月初め）で日付を生成しています。startは範囲の開始日、endは範囲の終了日、periodsは生成する日付の数、freqは頻度です。
# 頻度の指定には様々なオプションがあります（'D'は日、'2D'は2日ごと、'MS'は月初めなど）。生成された日付はDatetimeIndexとして取得できます。
