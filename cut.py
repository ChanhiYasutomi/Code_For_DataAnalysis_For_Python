import pandas as pd
import numpy as np

# ダミーデータを作成
data = {'purchase_count': np.random.randint(0, 1000, size=10)}
df = pd.DataFrame(data)

df.iloc[0,0] = 0
df.iloc[1,0] = 200
df.iloc[2,0] = 201
df.iloc[3,0] = 400

# =============================================
# パラメータ
# =============================================
columname = 'purchase_count'
start     = 0
bin       = 200
max       = df[columname].max()
# =============================================

# 区間のラベルを作成
labels = [f'{i+1}-{i+bin}' for i in range(start, max+1, bin)]
# {i+1} と書かざるを得ないため、0 スタートにならない。よってここだけ上書きして修正する
labels[0] = f'{start}-{start+bin}'

# purchase_countカラムを0始まりでbinずつに区切った値を作成
# include_lowest=true で下側の区間に含まれるようにする
# df[columname+'_bins'] = pd.cut(df[columname], bins=range(start, max + bin + 1, bin), labels=labels)
df[columname+'_bins'] = pd.cut(df[columname], bins=range(start, max + bin + 1, bin), labels=labels, include_lowest=True)

# 欠損数
print(df[columname+'_bins'].isnull().sum())

# このコードは、指定した列（purchase_count）の値を特定のビン（区間）に分割して新しい列を作成し、各値を対応するビンに配置しています。以下にコードの詳細と出力の説明を示します。
# pd.DataFrame(data) を使用してダミーデータフレーム df を作成します。このデータフレームには purchase_count カラムが含まれています。

# ビンのパラメータを指定します。
# start: ビンの開始値
# bin: 各ビンの幅
# max: データセット内の最大値
# 区間のラベルを作成します。このラベルは各ビンの範囲を表します。例えば、"0-200" は 0 から 200 までの値が含まれるビンを表します。ただし、0 から始まるビンのラベルは "{i+1}-{i+bin}" の形式になります。

# pd.cut() 関数を使用して、purchase_count カラムの値をビンに分割し、新しいカラム purchase_count_bins に格納します。bins パラメータには各ビンの境界を示すリストが指定され、labels パラメータにはビンのラベルが指定されます。include_lowest=True に設定されているため、各ビンは下側の区間に含まれます。

# 最後に、purchase_count_bins カラム内の欠損値の数を出力します。この行は、欠損値の数が表示されます。

# このコードを実行すると、purchase_count_bins カラムが作成され、各値が対応するビンに配置されます。また、欠損値の数も表示されます。

# 丸める場合は以下の処理を追加
# 新しいカテゴリーを追加するときはまずstr型に修正する
# Categoricalデータ型からstr型に変換
df[columname+'_bins'] = df[columname+'_bins'].astype(str)

# 下限の上書き
df.loc[df[columname] <= 200, columname+'_bins'] = '-200'

# 上限の上書き
df.loc[df[columname] >=750, columname+'_bins'] = '750-'

# 大小関係を考慮して、良い感じにクロス集計するにはカテゴリ型にしないといけないので戻す
df[columname+'_bins'] = df[columname+'_bins'].astype('category')

df_grouped = df.groupby([columname+'_bins'])[columname].agg(["count","sum"])

# 提供されたコードは、ビンに値を丸める追加の処理を含んでいます。具体的には、ビン内の値をカテゴリー（Categorical）データ型に変換し、一部の値を指定した条件で上書きしています。その後、カテゴリー型に戻し、クロス集計を行っています。以下に詳細な説明を示します。

# df[columname+'_bins'] = df[columname+'_bins'].astype(str):
# purchase_count_bins カラム内の値を文字列型（str）に変換します。これは後で一部の値を上書きする際に必要です。

# df.loc[df[columname] <= 200, columname+'_bins'] = '-200':
# purchase_count カラムの値が 200 以下の場合、対応する行の purchase_count_bins カラムの値を '-200' に上書きします。つまり、200 以下の値はビン '-200' に分類されます。

# df.loc[df[columname] >=750, columname+'_bins'] = '750-':
# purchase_count カラムの値が 750 以上の場合、対応する行の purchase_count_bins カラムの値を '750-' に上書きします。つまり、750 以上の値はビン '750-' に分類されます。

# df[columname+'_bins'] = df[columname+'_bins'].astype('category'):
# 上記の操作で一時的に文字列型に変換した purchase_count_bins カラムの値を再度カテゴリー型に変換します。これは、大小関係を考慮してクロス集計を行うために必要なステップです。

# df_grouped = df.groupby([columname+'_bins'])[columname].agg(["count","sum"]):
# 最終的に、カテゴリー型に変換された purchase_count_bins カラムを使用して、purchase_count カラムのクロス集計を行います。各ビン内のデータ数（'count'）と合計値（'sum'）が計算されます。

# この追加の処理により、特定の条件に基づいて値をビンに配置し、クロス集計が実行されます。これにより、データのセグメンテーションや集計が行いやすくなります。


# 年齢を区間に分けて、新しいカラムage_groupを作成する
df['age_group'] = pd.cut(df['age'],
                          bins=[10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60,
                                65, 70, 75, 80, 85, 90, 95, 100, 105],
                          labels=['10-14', '15-19', '20-24', '25-29', '30-34',
                                  '35-39', '40-44', '45-49', '50-54', '55-59',
                                  '60-64', '65-69', '70-74', '75-79', '80-84',
                                  '85-89', '90-94', '95-99', '100-104'])

# このコードは、DataFrame df の 'age' カラムを区間に分け、新しい 'age_group' カラムを作成する方法を示しています。pd.cut 関数を使用して、'age' の値を指定した区間に分割し、それぞれの区間に対応するラベルを 'age_group' カラムに割り当てています。

# 具体的には、次の手順が行われています：
# pd.cut 関数を使用して、'age' カラムを指定した区間に分割します。bins パラメータには年齢の区間を指定し、labels パラメータには各区間に対応するラベルを指定しています。これにより、各行の年齢が対応する区間に分類されます。
# 結果として得られる区間に対応するラベルが、新しい 'age_group' カラムに割り当てられます。各行の 'age' に応じて、対応する 'age_group' ラベルが格納されます。
# このようにして、DataFrame 内の年齢データを区間ごとに分類し、新しい 'age_group' カラムを作成します。この 'age_group' カラムを使用することで、年齢に基づいた集計や可視化などの操作が簡単に行えるようになります。
