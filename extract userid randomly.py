# 以下のコードは、ランダムにユーザーIDを選択し、そのユーザーに関連するデータを抽出して表示するものです。

import random
import pandas as pd

# ダミーデータを作成
data = {
    'pre_user_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'value1': [10, 20, 15, 30, 25, 8, 18, 12, 35, 40],
    'value2': [5, 15, 10, 25, 20, 3, 8, 6, 30, 35]
}

# データフレームを作成
aaa = pd.DataFrame(data)

# ランダムにユーザーIDを選択するためのユーザーリスト
users_with_false_dummy = [1, 3, 5, 6, 8]  # 例としていくつかのユーザーIDをリストアップ

# 5回繰り返す
for i in range(2):
    
    # users_with_false_dummyからランダムにuser_idを1件抽出
    random_user_id = random.choice(users_with_false_dummy)

    print(f"Randomly selected user_id: {random_user_id}\n")
    
    # ユーザーIDに対応するデータを表示
    display(aaa[aaa.pre_user_id == random_user_id])
    print()

# このコードでは、users_with_false_dummy というユーザーIDのリストからランダムにユーザーIDを選択し、それに対応するデータを aaa データフレームから抽出して表示しています。このようにして、特定の条件を満たすユーザーのデータをランダムに選択して表示できます。
# このコードでは、pre_user_id を1から10までの10個のユーザーに対して拡張し、ランダムにユーザーIDを選択してそのユーザーに関連するデータを表示します。
