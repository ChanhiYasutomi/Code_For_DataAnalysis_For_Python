# クロス集計
pd.crosstab(dataframe['columns'], dataframe['columns']).reset_index()

# pd.crosstab(dataframe['columns_1'], dataframe['columns_2'], dataframe['columns'_3]).reset_index()のようにカラムが3つある場合に、
# dataframe['columns_1']かつdataframe['columns_2']の条件(行)でdataframe['columns'_3](列)のクロス集計になる。
