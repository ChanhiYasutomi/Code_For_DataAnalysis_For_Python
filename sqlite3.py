import sqlite3
import pandas as pd

# CSVファイルを読み込む
df_customers = pd.read_csv('customers.csv')
df_purchase_log = pd.read_csv('purchaseLogs.csv')

# データベースに接続
# SQLiteデータベースに接続します。sqlite3.connectメソッドを使用して、新しいデータベースファイル 'mydatabase.db' に接続します。このデータベースは既に存在する場合、それを開きます。
conn = sqlite3.connect('mydatabase.db')

# データフレームをSQLiteデータベースに挿入
# to_sqlメソッドを使用して、データフレームをSQLiteデータベースに挿入します。
# df_customersデータフレームは 'customers' テーブルに、df_purchase_logデータフレームは 'purchase_log' テーブルに挿入されます。
# if_exists='replace'は、すでにテーブルが存在する場合にテーブルを置き換えるオプションです。
# index=Falseは、データフレームのインデックスをデータベースに挿入しないように指定しています。
df_customers.to_sql('customers', conn, if_exists='replace', index=False)
df_purchase_log.to_sql('purchase_log', conn, if_exists='replace', index=False)

# example
query = """
    SELECT
      *
    FROM
      purchase_log as p
    LEFT JOIN
      customers as c
    ON
      c.CustomerID = p.CustomerID
"""

# データベースを閉じる
# データベース接続を閉じます。conn.close()を呼び出すことで、データベースへの接続が正しく閉じられます。
conn.close()
