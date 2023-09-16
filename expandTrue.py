# 分割される文字列が適切でない場合: もし df の中にハイフンが含まれていない場合、split メソッドはエラーを引き起こす可能性があります。適切な文字列が分割されることを確認してください。
# 新しい列名が適切でない場合: expand=True を使用すると、新しい列の名前が自動生成されます。これらの名前が適切でない場合、後続の処理に問題が発生する可能性があります。新しい列名が予想通りであることを確認してください。
# 以下に、具体的な例を示します。

import pandas as pd

# サンプルのデータ
data = {
    'df': ['apple-fruit', 'banana-fruit', 'carrot-vegetable']
}

df = pd.DataFrame(data)

# 'df' 列をハイフンで分割して新しい列に展開
split_df = df['df'].str.split("-", expand=True)

# このコードは、'df' 列をハイフンで分割し、新しい列に展開します。結果のDataFrame split_df には、分割された各部分文字列が新しい列として表示されます。ただし、適切なデータと列名を使用することが重要です。
