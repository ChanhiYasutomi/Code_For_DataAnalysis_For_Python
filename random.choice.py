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



# random.choice() 関数は、与えられたシーケンス（リストやタプルなどの iterable）からランダムに一つの要素を選択します。以下に random.choice() の具体例を示します：
import random

# random.choice() の具体例

# リストからランダムに一つの要素を選択
my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
random_fruit = random.choice(my_list)

# 結果を表示
# print(f'ランダムに選ばれたフルーツ: {random_fruit}')
# 出力:
# ランダムに選ばれたフルーツ: banana

# この例では、my_list というリストから random.choice() を使ってランダムに一つの要素を選択し、その結果を表示しています。毎回実行すると、選ばれる要素が異なります。
# random.choice() は、ランダムな選択が必要な場面で利用されます。例えば、ゲームやシャッフルのプロセス、ランダムなデータ生成などで使うことがあります。
