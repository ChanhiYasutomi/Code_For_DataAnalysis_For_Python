columns = ['word_1', 'word_2', 'word_3', 'word_4', 'word_5']
dataframe['cnt_dep'] = dataframe[columns].apply(lambda x: x.nunique(), axis=1)

