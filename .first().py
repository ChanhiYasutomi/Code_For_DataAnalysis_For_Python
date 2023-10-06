# .first()について具体例を挙げて説明して
# 例えば、以下のようなDataFrameがあるとしよう：
import pandas as pd

data = {'userid': [1, 1, 2, 2, 3],
        'subsc_id': [101, 102, 201, 202, 301]}

df = pd.DataFrame(data)
# このDataFrameは以下のようになる：

#    userid  subsc_id
# 0       1       101
# 1       1       102
# 2       2       201
# 3       2       202
# 4       3       301
# ここで、groupbyと.first()を使って各ユーザーごとに'subsc_id'の最初の値を取得すると：

result = df.groupby('userid')['subsc_id'].first()
# 結果は次のようになる：

# userid
# 1    101
# 2    201
# 3    301
# Name: subsc_id, dtype: int64
# この結果では、各ユーザーごとに最初の'subsc_id'が取得されているね。例えば、ユーザー1は101、ユーザー2は201、ユーザー3は301が取得されている。
