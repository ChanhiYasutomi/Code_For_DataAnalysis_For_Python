import random
from datetime import datetime, timedelta

def random_date(start, end):
    """startとendの差をday変換してランダムで選択して、startに加算"""
    delta = end - start
    int_delta = (delta.days)
    random_day = random.randrange(int_delta)

    return (start + timedelta(days=random_day)).strftime("%Y-%m-%d")

def random_id(n_size):
    return random.choice(range(n_size))

def create_dataset(d_length, n_size, start_day, end_day):
    """ datasetをつくる
    customer_id: user
    event_date: action(ログイン、特定のログなど、なにかしらの行動が発生した日)
    weekofyear: event_dateがその年の何週目にあたるか
    """
    d_list = []
    for _ in range(d_length):
        d_list.append([random_id(n_size),random_date(start_day, end_day)])
    # dataframeに変換
    df = pd.DataFrame(d_list, columns=["customer_id","event_date"])
    # event_dateがその年の何週目にあたるのかを算出
    df["weekofyear"] = pd.to_datetime(df["event_date"]).dt.weekofyear

    return df

d1 = datetime.strptime('2018-01-01', '%Y-%m-%d')
d2 = datetime.strptime('2018-06-01', '%Y-%m-%d')
df = create_dataset(20000, n_size=1000, start_day = d1, end_day = d2)
df.head()


# 提供されたコードは、Pythonでデータセットを生成するための関数とそれを使用してデータセットを作成する処理です。以下に各部分の解説を記載します。
# random_date 関数:
# 開始日 (start) から終了日 (end) までの範囲でランダムな日付を生成します。
# delta には end - start の差が格納され、それを日数に変換して int_delta に代入します。
# random.randrange(int_delta) により、0から int_delta-1 までのランダムな整数を生成し、それを日数として start に加算します。
# 生成された日付は "%Y-%m-%d" の形式にフォーマットされて返されます。

# random_id 関数:
# 0から n_size-1 までの範囲からランダムに整数を選択して返します。
# これを利用してランダムな customer_id を生成します。

# create_dataset 関数:
# d_length 回、random_id と random_date を使用して (customer_id, event_date) のペアを生成し、リスト d_list に格納します。
# これらのペアを列 "customer_id" と "event_date" に持つデータフレームを作成します。
# "event_date" を日付型に変換し、その年の何週目にあたるかを計算して新しい列 "weekofyear" に追加します。

# d1 および d2:
# データセットの "event_date" 列に含まれる日付の範囲を指定しています。

# df:
# create_dataset 関数を使用して、20,000 行のデータフレームを生成しています。n_size は customer_id の候補者数です。
# このコードを実行すると、ランダムな customer_id と event_date が生成され、それに基づいてデータセットが作成されます。
# データフレームの先頭部分が df.head() で表示されます。
