import pandas as pd

# サンプルデータを含むデータフレームを作成
data = {
    'userid': [1, 1, 2, 2, 2, 3, 3, 4],
    'subscid': [1, 1, 1, 2, 2, 1, 2, 1],
    'flag': ['A', 'A', 'A', 'B', 'A', 'A', 'B', 'A']
}

df_subsc = pd.DataFrame(data)

# 重複行を削除し、最初の値を残す
df_no_duplicates = df_subsc[~df_subsc.isin(df_subsc.drop_duplicates(subset=['userid', 'subscid', 'flag'])).all(1)]

display(df_no_duplicates)

# このコードは、Pandasライブラリを使用してデータフレーム内の重複行を検出し、最初の値を残す方法を示しています。以下にコードの各部分とそれが行うことについて説明します：

# import pandas as pd：Pandasライブラリをインポートします。
# サンプルデータを含むデータフレーム df_subsc を作成します。このデータフレームには 'userid'、'subscid'、および 'flag' の3つの列が含まれています。

# df_subsc.drop_duplicates(subset=['userid', 'subscid', 'flag'])：この部分は、指定した列（'userid'、'subscid'、'flag'）をキーとしてデータフレームの重複行を削除します。つまり、各ユーザー、サブスクリプション、およびフラグに対して最初の値を保持したデータフレームが生成されます。
# df_subsc.isin(...)：この部分は、元のデータフレーム df_subsc の各行が重複行と一致するかどうかを示すブール値のデータフレームを作成します。各行が重複行と一致する場合はTrue、一致しない場合はFalseとなります。
# .all(1)：この部分は、各行に対して全ての要素がTrueであるかどうかをチェックし、その結果に基づいて行を選択します。したがって、最終的な結果は、重複行を持たない行だけを含むデータフレームとなります。
# display(df_no_duplicates)：最終的な結果のデータフレーム df_no_duplicates を表示します。

# 具体的な例について考えてみましょう：
# データフレーム df_subsc が以下のようになっていると仮定します：

#    userid  subscid flag
# 0       1       1    A
# 1       1       1    A
# 2       2       1    A
# 3       2       2    B
# 4       2       2    A
# 5       3       1    A
# 6       3       2    B
# 7       4       1    A

# この場合、最初に重複行を削除したデータフレームは次のようになります：

#    userid  subscid flag
# 0       1       1    A
# 2       2       1    A
# 3       2       2    B
# 5       3       1    A
# 6       3       2    B
# 7       4       1    A
# 次に、df_subsc.isin(...) を計算すると、各行が重複行と一致するかどうかを示すブール値のデータフレームが得られます：

#    userid  subscid  flag
# 0    True     True  True
# 1   False    False  True
# 2    True     True  True
# 3    True     True  True
# 4   False    False  True
# 5    True     True  True
# 6    True     True  True
# 7    True     True  True
# 最後に、.all(1) を適用して、各行がすべてTrueであるかどうかをチェックし、その結果に基づいて行を選択します。したがって、最終的な結果は次のようになります：

#    userid  subscid flag
# 1       1       1    A
# 4       2       2    A
# このようにして、重複行を持たない行だけを残すことができます。
