# category
category_tmp = video_tags[['Categories',"ID"]].drop_duplicates()
merge_tmp_category = pd.merge(video_log[columns], category_tmp  ,how = 'left', on = 'ID')

a = merge_tmp_category[['ID','Categories']].drop_duplicates()
b = dataframe.merge(a, how = 'inner', on = 'Id')

b['Categories'] = b['Categories'].fillna(0)
pd.crosstab(b['Categories'],b['frequency']).reset_index()
