# iterrows() は、Pandasデータフレーム内の各行を反復処理するためのメソッドです。各反復ステップで、現在の行のインデックスとデータを取得できます。
# ただし、iterrows() を使用する際には注意が必要で、大規模なデータセットでは効率が悪いことがあります。代わりに、apply() やベクトル化された操作を検討することが一般的です。以下は iterrows() の具体的な例です。

import pandas as pd

# サンプルのデータフレームを作成
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22]
}

df = pd.DataFrame(data)

# iterrows() を使用してデータフレームの各行を反復処理
for index, row in df.iterrows():
    name = row['Name']
    age = row['Age']
    print(f'Index: {index}, Name: {name}, Age: {age}')
  
# このコードでは、以下のことが行われています：
# サンプルのデータフレーム df を作成します。このデータフレームには2つの列 'Name' と 'Age' が含まれています。
# iterrows() メソッドを使用して、データフレームの各行を反復処理します。
# 各反復ステップで、現在の行のインデックスとデータが index と row に格納されます。
# 各行の 'Name' と 'Age' を取得し、それを表示しています。
# 出力結果は次のようになります：

# Index: 0, Name: Alice, Age: 25
# Index: 1, Name: Bob, Age: 30
# Index: 2, Name: Charlie, Age: 22

# iterrows() を使用することで、データフレーム内の各行に対して繰り返し処理を行うことができます。ただし、大規模なデータセットでは処理が遅くなる可能性があるため、注意が必要です。データセットが大きい場合は、より効率的な方法を検討することが重要です。
