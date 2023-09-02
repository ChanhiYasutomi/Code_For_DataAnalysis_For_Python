# technician
technician_tmp = df_technician[['ID','technician　Name']].drop_duplicates()　#ユニークにしたい
merge_tmp_technician = pd.merge(video_log[columns], technician_tmp ,how = 'left', on = 'ID') #1対1の関係だからこれで大丈夫(レコード数が増えない。) 1対Nである場合は(データが重複している場合)はデータが増えてしまう。

a = merge_tmp_technician[['Id','technician Name']].drop_duplicates()
b = dataframe.merge(a, how = 'inner', on = 'Id')

b['technician Name'] = b['technician Name'].fillna(0)
pd.crosstab(b['technician Name'],b['frequency']).reset_index()

# category
category_tmp = df_video_tags[['Categories',"ID"]].drop_duplicates()　#ユニークにしたい
merge_tmp_category = pd.merge(video_log[columns], category_tmp  ,how = 'left', on = 'ID')　#1対1の関係だからこれで大丈夫(レコード数が増えない。) 1対Nである場合は(データが重複している場合)はデータが増えてしまう。

a = merge_tmp_category[['Id','Categories']].drop_duplicates()
b = dataframe.merge(a, how = 'inner', on = 'ID')

b['Categories'] = b['Categories'].fillna(0)
pd.crosstab(b['Categories'],b['frequency']).reset_index()

# tech
tech_tmp = df_video_tags[['tech name',"ID"]].drop_duplicates()　#ユニークにしたい
merge_tmp_tech = pd.merge(video_log[columns], tech_tmp  ,how = 'left', on = 'ID')　#1対1の関係だからこれで大丈夫(レコード数が増えない。) 1対Nである場合は(データが重複している場合)はデータが増えてしまう。

a = merge_tmp_tech[['Id','tech name']].drop_duplicates()
b = dataframe.merge(a, how = 'inner', on = 'ID')

b['tech name'] = b['tech name'].fillna(0)
pd.crosstab(b['tech name'],b['frequency']).reset_index()
