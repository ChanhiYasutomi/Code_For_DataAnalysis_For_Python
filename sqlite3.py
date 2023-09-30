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



# 必要なライブラリをインポート
import sqlite3

# データベースファイル名を指定
db_file = "your_database.db"  # データベースファイル名を適宜変更してください

# SQL CREATE文を指定
create_table_sql = """
CREATE TABLE your_table_name (
  userid varchar(64),
  date date,
  product_name varchar(255),
  product_name_shorten varchar(255),
  order_id varchar(64),
  price decimal(8,2),
  age smallint,
  era smallint,
  address varchar(80),
  coupon_code varchar(50),
  coupon_discount int,
  usable_days smallint,
  birth_yyyymm varchar(7),
  sex varchar(6),
  pay_code varchar(10),
  total_postage decimal(8,2),
  mailmaga_flag tinyint,
  subsc_goods_flag tinyint,
  subsc_id varchar(64),
  sales decimal(10,2),
  product_of_how_many_days smallint,
);
"""

# SQLiteデータベースを作成しCREATE文を実行
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute(create_table_sql)
conn.commit()
conn.close()

print("テーブルが作成されました。")



# データの型を調べる
# データベースファイル名を指定
db_file = "your_database.db"

# SQLiteデータベースに接続
conn = sqlite3.connect(db_file)

# カラム情報を取得するSQLクエリ
query = "PRAGMA table_info(your_table_name);"

# SQLクエリを実行して結果を取得
cursor = conn.execute(query)
column_info = cursor.fetchall()

# 取得したカラム情報を表示
for column in column_info:
    print(column)

# データベース接続を閉じる
conn.close()



# 必要なライブラリをインポート
import sqlite3

# データベースファイル名を指定
db_file = "your_database.db"  # 既存のデータベースファイル名に合わせて変更してください

# SQLiteデータベースに接続
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# テーブルに仮想のデータを挿入
insert_data_sql = """
INSERT INTO your_table_name (
  userid, dateoftransactionconfirm_jst_date, productname, productname_shorten, order_id,
  noofboxpurchased, price, age, era, address, coupon_info, coupon_discount, product_use_days,
  product_code, birth_yyyymm, sex, noofpurchases, pay_code, total_postage, mailmaga_flag,
  subsc_goods_flag, subsc_id, sales, purchase_of_how_many_days, crm_flag, previous_crm_flag
) VALUES (
  'user1', '2023-09-25', 'Product A', 'Prod A', 'order123', 2, 50.0, 35, 2, '123 Main St',
  'Coupon1', 10, 30, 'P123', '199001', 'Male', 5, 'PayCode1', 5.0, 1, 1, 'Subsc123',
  100.0, 10, 1, 0
);

"""

# トランザクションをコミットしてデータを保存
conn.execute(insert_data_sql)
conn.commit()

# データベース接続を閉じる
conn.close()

print("データが挿入されました。")



# データベースに再度接続
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# データを取得して表示する例
query = "SELECT * FROM your_table_name;"
cursor.execute(query)

# データをフェッチして表示
for row in cursor.fetchall():
    print(row)

# データベース接続を閉じる
conn.close()



# SQLiteデータベースに接続
conn = sqlite3.connect(db_file)

# SQLクエリを実行し、データをデータフレームに読み込む
query = "SELECT * FROM your_table_name;"
df = pd.read_sql_query(query, conn)

# データベース接続を閉じる
conn.close()

# データフレームを表示
display(df)
