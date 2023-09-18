# 以下は、pd.options.display.float_format を使用してDataFrame内の浮動小数点数をパーセンテージ形式で表示する具体的なPythonコードの例です。

import pandas as pd

# サンプルのDataFrameを作成
data = {'Category': ['A', 'B', 'C'],
        'Percentage': [0.12345, 0.45678, 0.78901]}

df = pd.DataFrame(data)

# 割合を % 表記に変更
pd.options.display.float_format = '{:.1%}'.format

# DataFrameを表示
print("DataFrame with Percentage Format:")
display(df)

# 以後は、% 表記をキャンセル
pd.options.display.float_format = None

# 再度DataFrameを表示（通常の数値形式）
print("\nDataFrame with Default Number Format:")
display(df)

# このコードでは、まずpd.options.display.float_format を使用してパーセンテージ形式（小数点以下1桁まで表示）に設定します。
# 次に、サンプルのDataFrame df を表示し、'Percentage' 列がパーセンテージ形式で表示されます。最後に、pd.options.display.float_format を None に設定して、通常の数値形式に戻します。

# 実行結果は以下のようになります：

# DataFrame with Percentage Format:
#   Category Percentage
# 0        A      12.3%
# 1        B      45.7%
# 2        C      78.9%

# DataFrame with Default Number Format:
#   Category  Percentage
# 0        A     0.12345
# 1        B     0.45678
# 2        C     0.78901

# 上記のコードにより、特定の部分で表示形式を一時的に変更し、必要に応じて元に戻す方法が示されています。
