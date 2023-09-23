import pandas as pd

# 仮のデータフレームを作成
data = {'userid': [1, 1, 2, 2, 3, 3, 4, 4],
        'product_id': ['A', 'B', 'A', 'A', 'A', 'B', 'C', 'C']}
df = pd.DataFrame(data)

# ユーザーごとの購入した商品の種類数をカウントし、1つの商品のみを購入したユーザーを抽出
user_purchase_counts = df.groupby('userid')['product_id'].nunique()
valid_users = user_purchase_counts[user_purchase_counts == 1].index

# 条件を満たすユーザーのみを残して新しいデータフレームを作成
filtered_df = df[df['userid'].isin(valid_users)].drop_duplicates()

# このPythonコードは、与えられたデータフレームから特定の条件を満たすユーザーを抽出し、新しいデータフレームを作成するものです。具体的なステップとコードの説明は以下の通りです：
# まず、仮のデータフレーム df を作成します。このデータフレームには、ユーザーID（'userid'列）と購入した商品ID（'product_id'列）が含まれています。
# groupbyメソッドを使用して、ユーザーごとに購入した異なる商品の数をカウントします。これにより、各ユーザーが異なる商品の数が計算されます。user_purchase_counts変数には、ユーザーIDをインデックスとし、対応するユーザーが購入した異なる商品の数が含まれます。
# user_purchase_countsから、購入した商品の数が1つだけ（つまり、1つの商品のみを購入したユーザー）のユーザーのインデックスを抽出します。これは user_purchase_counts[user_purchase_counts == 1].index で行われます。
# 条件を満たすユーザーのインデックスを使用して、元のデータフレーム df から該当ユーザーの行を抽出します。df['userid'].isin(valid_users)は、条件を満たすユーザーに対応する行をフィルタリングし、.drop_duplicates()メソッドによって重複行を削除します。このようにして、条件を満たすユーザーだけが残る新しいデータフレーム filtered_df が作成されます。
# 結果的に、filtered_dfには、1つの商品のみを購入したユーザーに関連するデータが含まれることになります。
