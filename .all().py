# .all() メソッドは、Pandasデータフレームやシリーズ内のブール値を持つ要素がすべてTrueであるかどうかを確認するために使用されます。具体的な例を挙げて説明しましょう。
# 以下は、.all() メソッドの具体的な例です：

import pandas as pd
# サンプルデータを含むデータフレームを作成
data = {
    'A': [True, True, True, True],
    'B': [False, False, False, True],
    'C': [False, False, False, False]
}

df = pd.DataFrame(data)

# 各列に対して.all()メソッドを適用し、すべての要素がTrueであるかどうかを確認
column_A_result = df['A'].all()
column_B_result = df['B'].all()
column_C_result = df['C'].all()

display(column_A_result)
display(column_B_result)
display(column_C_result)

# このコードでは、3つの列（'A'、'B'、'C'）が含まれるデータフレーム df を作成し、それぞれの列に対して.all() メソッドを適用しています。
# 出力は次のようになります：

True
False
False

# この結果からわかるように、各列に対して.all() メソッドを適用した結果、すべての要素がTrueでないため、各列の結果はすべてFalseとなっています。
# このように、.all() メソッドは、列やシリーズ内の要素がすべてTrueであるかどうかを簡単に確認するために役立ちます。
