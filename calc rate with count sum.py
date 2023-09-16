import pandas as pd

# 提供されたデータ
data = {
    'sex': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'age_1st': ['25-34', '18-24', '25-34', '18-24', '35-44', '25-34'],
    'second_flg': [1, 1, 0, 1, 1, 0]
}

# データフレームを作成
df = pd.DataFrame(data)

# 新しいデータを作成
new_data = {
    'sex': ['Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Male', 'Female'],
    'age_1st': ['18-24', '25-34', '35-44', '18-24', '25-34', '35-44', '25-34', '18-24'],
    'second_flg': [0, 1, 1, 1, 0, 0, 1, 1]
}

# 新しいデータを含むデータフレームを作成
df = df.append(pd.DataFrame(new_data), ignore_index=True)

# 性別（'sex'）と初めての年齢層（'age_1st'）でグループ化し、購買回数と購買回数の合計を計算
result = df.groupby(['sex', 'age_1st'], dropna=False)['second_flg'].agg(["count", "sum"])

# 購買率を計算
result['purchase_rate'] = result['sum'] / result['count']
