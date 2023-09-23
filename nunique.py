# df.nunique() は、PandasのDataFrameオブジェクトに対して使用できるメソッドの一つで、各列（特徴量）においてユニークな（異なる）値の数を返すために使用されます。具体的な例を示します。
# 例として、サンプルのDataFrameを作成し、nunique メソッドを使用して各列のユニークな値の数を取得します。
import pandas as pd

# サンプルのDataFrameを作成
data = {'A': [1, 2, 2, 3, 4],
        'B': ['apple', 'banana', 'apple', 'cherry', 'banana'],
        'C': [10.5, 20.3, 15.8, 10.5, 30.1]}

df = pd.DataFrame(data)

# 各列のユニークな値の数を取得
unique_counts = df.nunique()

# 結果を表示
print(unique_counts)

# このコードの説明：
# data ディクショナリを使用してサンプルのDataFrame df を作成します。df には整数列 'A'、文字列列 'B'、浮動小数点数列 'C' が含まれます。
# df.nunique() メソッドを使用して、各列のユニークな値の数を計算します。このメソッドは、各列のユニークな値の数を含むシリーズ（Series）を返します。
# 結果を unique_counts 変数に格納します。
# 最後に print(unique_counts) を使用して、各列のユニークな値の数を表示します。
# 出力は以下のようになります：

# A    4
# B    3
# C    4
# dtype: int64

# この結果から、'A' 列には4つのユニークな値、'B' 列には3つのユニークな値、'C' 列には4つのユニークな値があることがわかります。この情報は、データの特性を理解し、データの前処理や分析の際に役立ちます。




