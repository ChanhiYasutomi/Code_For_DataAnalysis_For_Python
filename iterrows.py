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



# このコードは、Pandasを使用してデータフレームをグループ化し、各グループ内の行を反復処理する例です。具体的には、userid 列を使用してデータフレームをグループ化し、各グループ内の行を取得しています。
import pandas as pd

# サンプルデータフレームを作成
data = {
    'userid': [1, 1, 2, 2, 2],
    'value': [10, 20, 30, 40, 50]
}

df = pd.DataFrame(data)

# useridでグループ化
# df.groupby('userid') を使用して、userid 列を基準にデータフレームをグループ化します。これにより、異なる userid の値を持つ行が異なるグループに分割されます。
groups = df.groupby('userid')

# 各グループの行を反復処理
# for key, group in groups: ループを使用して、各グループ内のデータにアクセスします。key にはグループのキー（userid の値）が格納され、group には該当するグループのデータフレームが格納されます。
# 各グループ内の行を反復処理するためのさらなる for index, row in group.iterrows(): ループを使用します。index には行のインデックスが格納され、row には行のデータが格納されます。
# 各行の情報を表示します。この場合、グループごとに userid と value の値が表示されます。
for key, group in groups:
    print(f'Group with userid {key}:')
    for index, row in group.iterrows():
        print(f'Index: {index}, Value: {row["value"]}')
    print()

# 出力結果は以下のようになります：

# Group with userid 1:
# Index: 0, Value: 10
# Index: 1, Value: 20

# Group with userid 2:
# Index: 2, Value: 30
# Index: 3, Value: 40
# Index: 4, Value: 50

# このように、groupby メソッドを使用してデータフレームをグループ化し、各グループ内の行を反復処理することで、異なるグループ内のデータにアクセスできます。
