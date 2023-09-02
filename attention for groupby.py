# (※要注意)
# 以下をId(ユニーク)と属性で分けている理由としてdataframe.groupby([['Id','attribute_1', 'attribute_2', 'attribute_3','attribute_n']])[columns].sum().reset_index()のようにgroubyをしたら、nullの部分がまとめてグループ化されるため母数が減少するため。
# そのためIdと属性を分割し、後にinner joinしている。
columns = ['2023-01', '2023-02', '2023-03', '2023-04', '2023-05', '2023-06', '2023-07', '2023-08', '2023-09', '2023-10', '2023-11', '2023-12']
only_id = dataframe.groupby(['Id'])[columns].sum().reset_index()　# nullがないことが前提(あるいは処理済み)
attribute = dataframe[['Id','attribute_1', 'attribute_2', 'attribute_3','attribute_n']].drop_duplicates()

dataframe = pd.merge(only_id, attribute, how = 'inner',left_on='Id',right_on='Id') # inner joinした理由はユニークであり、欠損がなかったから(確かnull処理はしていない。)

# Group by null どうなる？
# GROUP BY 節にリストした列において、NULL 値を含む各行は単一グループに属します。 つまり、すべての NULL 値がまとめてグループ化されます。
# これにより母数のレコード数が減る現象が起きる(※要注意)

# apply loop processing for selected columns
# 値が1以上であれば1を付与し、それ以外は0を付与する。
for column in columns:
    dataframe[columns] = dataframe[columns].apply(lambda x: 1 if x >= 1 else 0)

# 行方向にcolumnsの値をsumし、sum_visitに格納。
dataframe['sum_visit'] = dataframe[columns].sum(axis=1).astype(int)

# sum_visitに格納された値が数字の範囲であれば '~頻度'を付与してfrequencyに格納。
dataframe['frequency'] = dataframe['sum_visit'].apply(lambda row: '高頻度' if 5 <= row <= 7 else
                                                                  '中頻度' if 3 <= row <= 4 else
                                                                  '低頻度' if 1 <= row <= 2 else
                                                                  '未視聴')
