# isin()は、Pandasライブラリで提供されている関数で、データフレーム（DataFrame）やシリーズ（Series）内の要素が指定したリストや配列に含まれているかどうかを確認するために使用されます。

import pandas as pd

data = {'名前': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        '年齢': [25, 30, 22, 35, 28],
        '都市': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Chicago']}

df = pd.DataFrame(data)

# 例 1: 特定の都市に住んでいる行を抽出する
cities_to_check = ['New York', 'Chicago']

# '都市'列が'New York'または'Chicago'の行を抽出
filtered_df = df[df['都市'].isin(cities_to_check)]

# 例 2: 特定の名前の行を抽出する
names_to_check = ['Alice', 'David', 'Frank']

# '名前'列が'Alice'または'David'の行を抽出
filtered_df = df[df['名前'].isin(names_to_check)]

# 上記のコードでは、isin()を使用して、'名前'列が'Alice'または'David'の行を抽出しました。指定された名前に一致する行だけが選択されました。
# このように、isin()を使用すると、データフレーム内の特定の値が含まれている行を簡単に抽出できます。
