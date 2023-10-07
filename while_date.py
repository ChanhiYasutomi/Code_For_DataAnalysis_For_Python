# 提供されたコードの具体例を挙げて説明します。以下のコードは、日付範囲を指定してデータフレームを加工し、その結果を新しいデータフレームに連結する例です。
# まず、以下のサンプルデータを持つデータフレーム df を作成します：
import pandas as pd

data = {
    'date': pd.date_range(start='2021-01-01', end='2021-12-31'),
    'product': ['subscA', 'subscB', 'productX', 'subscA', 'productY'] * 73,  # 日付範囲を埋めるために繰り返し
    'code': ['A', 'B', 'X', 'A', 'Y'] * 73,
    'userid': [101, 102, 103, 101, 104] * 73,  # 日付範囲を埋めるために繰り返し
}

df = pd.DataFrame(data)

# このデータフレームには 'date'（日付）、'product'（製品名）、'code'（コード）、'userid'（ユーザーID）の列が含まれています。
# 次に、提供されたコードを使用して日付範囲を設定し、データを加工および計算します。
import datetime

# 空のデータフレームを作成
subsc_result_df = pd.DataFrame()

# 初期の日付
target_date = datetime.datetime(2021, 3, 29)
start_date = target_date - pd.DateOffset(days=365)

# 1日ごとにずらしながらデータを加工・格納
while target_date <= datetime.datetime(2023, 9, 20):
    # （中略）データのコピーと期間に合わせたデータの抽出、計算を行う部分

    # 結果をresult_dfに追加
    subsc_result_df = pd.concat([subsc_result_df, df])

    # 日付を1日進める
    target_date += datetime.timedelta(days=1)
    start_date += datetime.timedelta(days=1)
  
# # このループは、target_date が datetime.datetime(2023, 9, 20) に達するまで続き、各日付範囲でデータを抽出し、計算した結果を subsc_result_df に連結しています。
# 結果のデータフレーム subsc_result_df は、各日付範囲ごとに 'subsc_product'、'unique_cnt_subsc_userid'、'not_subsc_product'、'unique_cnt_not_subsc_userid'、'subsc_rate' の列を持ち、最終的な結果が格納されます。
# このように、提供されたコードは日付範囲を操作し、データの加工と計算を行うためのループ処理を示しており、実際のデータ分析や集計に役立つ方法です。



mport datetime
# 空のデータフレームを作成
subsc_result_df = pd.DataFrame()

# 初期の日付
# (2021/3/29 - 365日) ~ 2021/3/29(target_date) スタートで、1日ごとにずらして、データを加工・格納を
# (2023/9/20 - 365日) ~ 2023/9/20(target_date) まで行う。
target_date = datetime.datetime(2021, 3, 29)
start_date = target_date - pd.DateOffset(days=365)

# 1日ごとにずらしながらデータを加工・格納
while target_date <= datetime.datetime(2023, 9, 20):
    
    # データのコピー（元データを保持するため）
    data_unit = df.copy()
    data_unit['date'] = pd.to_datetime(data_unit['date'])

    # 期間に合わせてデータを抽出
    data_unit_filtered = data_unit[(data_unit['date'] >= start_date) & (data_unit['date'] <= target_date)]

    # 製品ごとでsubscの文字がついているユニークなユーザカウント数
    subsc = data_unit_filtered[data_unit_filtered ['product'].str.contains('subsc')]
    df_subsc = subsc.groupby(['product', 'code'], dropna = False, as_index = False)['userid'].nunique().sort_values('product').rename(columns={'userid': 'unique_cnt_subsc_userid'})
    df_subsc.columns = ['product', 'code', 'unique_cnt_subsc_userid']

    # 結合ため末尾のJを除外する(subscという意味)
    df_subsc['code'] = df_subsc['code'].str[:-1]
    
    # subsc以外の通常商品を購入したユーザー数
    not_subsc = data_unit_filtered[~data_unit_filtered['product'].str.contains('subsc')]
    df_groupby_not_subsc = not_subsc.groupby(['product', 'code'], dropna = False, as_index = False)['userid'].nunique().sort_values('product').rename(columns={'userid': 'unique_cnt_not_subsc_userid'})
    df_groupby_not_subsc.columns = ['product', 'code', 'unique_cnt_not_subsc_userid']

    # outerで結合
    df_subsc_rate = df_subsc.merge(df_groupby_not_subsc, on = 'code' , how='outer').rename(columns={'product_x': 'subsc_product', 'product_y': 'not_subsc_product'})
    df_subsc_rate['target_date'] = target_date

    # 文字列は空文字で補完
    df_subsc_rate['subsc_product'] = df_subsc_rate['subsc_product'].fillna('')
    df_subsc_rate['not_subsc_product'] = df_subsc_rate['not_subsc_product'].fillna('')

    # 数値列は0で補完
    df_subsc_rate['unique_cnt_subsc_userid'] = df_subsc_rate['unique_cnt_subsc_userid'].fillna(0)
    df_subsc_rate['unique_cnt_not_subsc_userid'] = df_subsc_rate['unique_cnt_not_subsc_userid'].fillna(0)

    # subsc比率の算出
    df_subsc_rate['subsc_rate'] = (df_subsc_rate['unique_cnt_subsc_userid'] / (df_subsc_rate['unique_cnt_subsc_userid'] +  df_subsc_rate['unique_cnt_not_subsc_userid'])).round(3)
    df_subsc_rate = df_subsc_rate[['target_date', 'subsc_product', 'unique_cnt_subsc_userid','not_subsc_product', 'unique_cnt_not_subsc_userid', 'subsc_rate']]

    # 結果をresult_dfに追加
    subsc_result_df = pd.concat([subsc_result_df, df_subsc_rate])

    # 日付を1日進める
    target_date += datetime.timedelta(days=1)
    start_date += datetime.timedelta(days=1)

# 結果を表示
# 提供されたコードは、日付範囲を指定してデータフレームを加工し、その結果を新しいデータフレームに連結する操作を示しています。以下に、コードの概要と各部分の説明を示します。
# 空のデータフレーム subsc_result_df を作成します。
# target_date を datetime.datetime(2021, 3, 29) に設定し、start_date を target_date から365日前の日付に設定します。これにより、処理を開始する日付範囲が設定されます。
# while ループを使用して、target_date が datetime.datetime(2023, 9, 20) に達するまでデータ加工を繰り返します。
# データのコピーを作成し、日付列を日付型に変換します。
# 指定した期間内のデータを抽出します。start_date から target_date までの範囲のデータを抽出します。
# 'subsc' という文字列を含む 'product' 列を持つユニークなユーザー数を計算します。この部分で df_subsc データフレームが作成されます。
# 'code' 列の末尾の 'J' を削除します。
# 'subsc' 以外の通常商品を購入したユーザー数を計算します。この部分で df_groupby_not_subsc データフレームが作成されます。
# 'code' 列をキーにして 'df_subsc' と 'df_groupby_not_subsc' を結合します。外部結合（'outer'）を使用します。
# 結合後のデータフレームを加工し、欠損値を補完します。
# 'subsc_rate' 列を計算し、必要な列を選択して 'df_subsc_rate' データフレームを作成します。
# 結果を subsc_result_df に連結します。
# target_date と start_date を1日進め、次の日付範囲での処理を準備します。
# ループが終了した後、subsc_result_df にはすべての日付範囲での計算結果が含まれ、最終的な結果が表示されます。
# このコードは、日付範囲をループしてデータの加工と計算を行い、結果を新しいデータフレームにまとめるための効果的な方法を示しています。データ分析や集計の一部として、日付範囲ごとにデータを操作する場合に役立つアプローチです。
