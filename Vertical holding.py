# 特定のカラムを縦持ちにして新しいカラムを生成
columns = ['word_1', 'word_2', 'word_3', 'word_4', 'word_5']
df_melted = dataframe.melt(id_vars=['Id'], value_vars=columns, value_name='dep').dropna(subset=['dep'])

# 元のデータフレームと結合
result = pd.merge(dataframe, df_melted, on='Id', how='outer')
