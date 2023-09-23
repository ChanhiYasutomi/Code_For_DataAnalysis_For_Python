# カテゴリの集約
# 所属するデータがあまりにも少ないカテゴリを使って学習を行うと、過学習のリスクが高まります。
# データの少ないカテゴリは、「その他」のようなカテゴリに集約してしまいましょう。

df['currency'].value_counts() 

# USD    21171
# GBP     2486
# EUR     1190
# CAD     1116
# AUD      557
# MXN      139
# SEK      126
# NZD       95
# DKK       80
# NOK       61
# HKD       54
# CHF       42
# SGD       35
# JPY        3
# Name: currency, dtype: int64

# AUD以下のカテゴリはデータ数が少ないことがわかります。よって、ここでは、これらを「Others」としてまとめます。

def others(currency):
    return np.where((currency == 'MXN') | (currency == 'SEK') | (currency == 'NZD') | (currency == 'DKK') |
                    (currency == 'NOK') | (currency == 'HKD') | (currency == 'CHF') | (currency == 'SGD') |
                    (currency == 'JPY'), 'Others', currency)
  
df['currency'] = others(df['currency'])

# df['currency'].value_counts()
# USD       21171
# GBP        2486
# EUR        1190
# CAD        1116
# Others      635
# AUD         557
# Name: currency, dtype: int64
