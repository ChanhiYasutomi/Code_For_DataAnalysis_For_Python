# facility
tmp['flg_facility'] = 0
tmp.loc[tmp['Name'].str.contains('facility'), 'flg_facility'] = 1
tmp.loc[tmp['Name_2'] == "facility_2", 'flg_facility'] = 1
pd.crosstab(tmp['frequency'], tmp['flg_facility'])

# この場合、tmpデータフレームが直接変更され、新しいデータフレームが返されない。
# tmp.loc[tmp['Name'].str.contains('facility'), 'flg_facility'] = 1
