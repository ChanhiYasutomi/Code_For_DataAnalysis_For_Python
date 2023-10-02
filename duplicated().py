import pandas as pd

data = {'userid': [1, 2, 3, 1, 4, 2, 5],
        'value': ['A', 'B', 'C', 'D', 'E', 'F', 'G']}
df = pd.DataFrame(data)
# この場合、userid列には重複する値があります。これをduplicated()メソッドを使って確認してみましょう：

duplicate_users = df[df['userid'].duplicated()]
display(duplicate_users)

duplicate_users_keep = df[df['userid'].duplicated(keep=False)]
display(duplicate_users_keep)

# これにより、重複するユーザIDを持つ行が抽出されます。結果は次のようになります：
#    userid value
# 0      1     A
# 1      2     B
# 3      1     D
# 5      2     F
# ここでkeep=Falseを指定することで、重複する全ての行が抽出されています。



# Pandasの.duplicated()メソッドを使用して、データフレーム内の重複した行を検出し、最初の値を残す方法は以下の通りです。keepパラメータを使って、どの値を保持するかを指定できます。keepパラメータをデフォルト値のままにすると、最初の値以外は重複とマークされ、それらは削除されます。
# 具体的な例を示します：
import pandas as pd

# サンプルデータを含むデータフレームを作成
data = {
    'A': [1, 2, 2, 3, 4, 4, 5],
    'B': ['x', 'y', 'y', 'z', 'w', 'w', 'z']
}

df = pd.DataFrame(data)

# 重複した行を検出し、最初の値を残す
df_no_duplicates = df[~df.duplicated(keep='first')]

print(df_no_duplicates)
# このコードを実行すると、重複行が削除され、最初の値のみが残るデータフレームが得られます。

# 出力は次のようになります：
#    A  B
# 0  1  x
# 1  2  y
# 3  3  z
# 4  4  w
# この例では、'A' 列で重複がある場合、最初の値を保持し、他の値は削除されました。
