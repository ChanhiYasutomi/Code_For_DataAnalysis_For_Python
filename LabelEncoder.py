# このPythonコードは、カテゴリカルな特徴量（列）を数値にエンコードするためにScikit-LearnのLabelEncoderを使用する例です。以下に具体例を示します：
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# サンプルのDataFrameを作成
data = {
    'category': ['A', 'B', 'C', 'A', 'B'],
    'main_category': ['X', 'Y', 'X', 'Y', 'Z'],
    'currency': ['USD', 'EUR', 'USD', 'GBP', 'EUR'],
    'state': ['success', 'failed', 'success', 'failed', 'success'],
    'country': ['USA', 'France', 'USA', 'UK', 'Germany']
}

df = pd.DataFrame(data)

# カテゴリカルな特徴量のリスト
cat_features = ['category', 'main_category', 'currency', 'state', 'country']

# LabelEncoderを使用してカテゴリカル特徴量をエンコード
for col in cat_features:
    lbl = LabelEncoder()  # LabelEncoderのインスタンスを作成
    df[col] = lbl.fit_transform(df[col].values)  # カテゴリカル特徴量をエンコード

# 結果を表示
display(df)

# 上記のコードでは、data ディクショナリからDataFrame df を作成し、カテゴリカルな特徴量が含まれています。cat_features リストには、エンコードしたいカテゴリカル特徴量の列名が含まれています。
# 次に、for ループを使用して各カテゴリカル特徴量に対してLabelEncoderを適用します。LabelEncoderは各カテゴリカル特徴量のユニークなカテゴリを整数にマッピングします。
# DataFrameの該当する列がエンコードされ、元のカテゴリカルな値が整数に置き換えられます。
# 最後に、変更後のDataFrameを表示して、カテゴリカル特徴量が数値にエンコードされたことを確認します。エンコードされた整数は、元のカテゴリカルな値とは異なり、数値計算で使用できるようになります。
