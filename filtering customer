# df_customerが元データ
# ユニークにしたデータフレームをdf_customer_tmpに格納
df_customer_tmp = df_customer['Id'].drop_duplicates()

# df_customer_tmpに対してdataframe_1~3をleft joinする
# dataframe_1~3はユニーク処理(drop_duplicates())かつnullを除外しており(dropna())、またフラグを付与している。そのフラグが付与されているレコードだけ抽出したい(フラグには1を付与) … ①
# この処理の目的はdf_customer_tmpに対して、dataframe_1~3にidがある顧客を対象にすることが目的である。 … ②
df_customer_tmp = pd.merge(df_customer_tmp, dataframe_1, how = 'left',left_on='Id', right_on='Id_tmp')
df_customer_tmp = pd.merge(df_customer_tmp, dataframe_2, how = 'left',left_on='Id', right_on='Id_tmp')
df_customer_tmp = pd.merge(df_customer_tmp, dataframe_3, how = 'left',left_on='Id', right_on='Id_tmp')

# df_customerに対して上記にてフィルタリングしたdf_customer_tmpをleft join
df_customer = pd.merge(df_customer, df_customer_tmp, how = 'left', on='Id')

# … ①の処理
dataframe = dataframe['Id'].dropna().drop_duplicates()
dataframe['flag_4'] = 1
df_customer = pd.merge(df_customer, dataframe, how = 'left', on='Id')

# 一つでもフラグ(1)があればその顧客を対象にする … ②
df_customer = df_customer[(df_customer['flag_1'] == 1) | (df_customer['flag_2'] == 1) | (df_customer['flag_3'] == 1) | (df_customer['flag_4'] == 1)]
