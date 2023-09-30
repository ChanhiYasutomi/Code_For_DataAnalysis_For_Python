import sqlalchemy as sa
# %pip install PyMySQL
import pymysql

# どんなテーブルが入っているか確認
url = '''xxx'''
engine = sa.create_engine(url, echo=False)

# select句, show句
query = f"""   
        show tables;
        """
df = pd.read_sql(query,con = engine)



# テーブルデータ自体を削除
url = '''xxx'''
engine = sa.create_engine(url, echo=False)
# 実行するときは慎重に
with engine.connect() as con:
    query = """
        DROP TABLE table_name;
        """
    con.execute(query)



# テーブル内のデータを削除
url = '''xxx'''
engine = sa.create_engine(url, echo=False)

# 実行するときは慎重に
with engine.connect() as con:
    query = """
        DELETE FROM table_name;
        """
    con.execute(query)



# テーブル情報を取得(カラム, データ型)
url = '''xxx'''

engine = sa.create_engine(url, echo=False)
query = f"""   
        desc table_name
        """
table_name = pd.read_sql(query,con = engine)

# sqlのdesc とはなに?
# SQLのDESCは、テーブルやビューの構造を表示するためのコマンドです。DESCは「DESCRIBE」または「DESCRIBE TABLE」という形で使用されることもあります。
# 主にデータベース内のテーブルやビューに関するメタデータ情報を取得するために使用されます。
# 具体的には、以下のように使用します：

# DESC table_name;
# ここで、table_nameはテーブルまたはビューの名前です。このコマンドを実行すると、指定したテーブルまたはビューのカラム（列）の情報が取得されます。これには、カラムの名前、データ型、制約（例: 主キー、外部キー）、デフォルト値などが含まれます。

# DESCコマンドを使用することで、テーブルの構造を理解し、クエリを作成する際に必要な情報を取得できます。データベース管理やクエリのデバッグなど、データベース作業のさまざまな場面で役立ちます。



# 読み込み
url = '''xxx'''

engine = sa.create_engine(url, echo=False)
query = f"""   
        SELECT
            *
        FROM 
            table_name
        """

df = pd.read_sql(query,con = engine)



# データベースにテーブルを格納
url = '''xxx'''
engine = sa.create_engine(url, echo=False)

# table_nameを database_table に挿入
with engine.connect() as con:
    table_name.to_sql('database_table', con=con, if_exists='append', index=False)
