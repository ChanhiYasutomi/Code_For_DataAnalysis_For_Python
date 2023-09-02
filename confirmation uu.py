# technician
technician_tmp = df_technician[['BC ID','technician　Name']].drop_duplicates()　#ユニークにしたい
merge_tmp_technician = pd.merge(video_log[columns], technician_tmp ,how = 'left', on = 'ID')

a = merge_tmp_technician[['Id','technician Name']].drop_duplicates()
b = dataframe.merge(a, how = 'inner', on = 'Id')

b['technician Name'] = b['technician Name'].fillna(0)
pd.crosstab(b['technician Name'],b['frequency']).reset_index()

# category
category_tmp = df_video_tags[['Categories',"BC ID"]].drop_duplicates()　#ユニークにしたい
merge_tmp_category = pd.merge(video_log[columns], category_tmp  ,how = 'left', on = 'ID')

a = merge_tmp_category[['Id','Content Categories']].drop_duplicates()
b = user_based_result.merge(a, how = 'inner', on = 'ID')

b['Categories'] = b['Categories'].fillna(0)
pd.crosstab(b['Categories'],b['frequency']).reset_index()

# tech
tech_tmp = df_video_tags[['tech name',"BC ID"]].drop_duplicates()　#ユニークにしたい
merge_tmp_tech = pd.merge(video_log[columns], tech_tmp  ,how = 'left', on = 'ID')

a = merge_tmp_tech[['Id','tech name']].drop_duplicates()
b = user_based_result.merge(a, how = 'inner', on = 'ID')

b['tech name'] = b['tech name'].fillna(0)
pd.crosstab(b['tech name'],b['frequency']).reset_index()
