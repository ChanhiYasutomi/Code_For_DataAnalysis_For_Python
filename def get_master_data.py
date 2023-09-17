def get_master_data():
    
    # S3 に接続
    print('S3に接続します')
    s3 = boto3.resource('s3')
    s3_bucket = s3.Bucket(BUCKET_NAME)

    print()
    print('現在の時刻 ……', datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))

    try:
        # キャンペーンマスタをダウンロードし保存する
        s3_bucket.download_file(xxx)
        # 保存したファイルの読み込み
        df_campaign_master = pd.read_csv(yyy)
    except Exception as e:
        raise Exception("S3のキャンペーンマスタの読み込みに失敗しました")
        
    return df_campaign_master

# このPythonコードは、AWS S3からキャンペーンマスターデータをダウンロードし、Pandasデータフレームに読み込むための関数です。以下は、このコードの概要と各部分の説明です。
# get_master_data() 関数の定義：
# get_master_data() 関数は、キャンペーンマスターデータを取得するための関数です。

# S3への接続：
# boto3 ライブラリを使用して、AWS S3に接続します。
# BUCKET_NAME は、S3バケットの名前を指定する変数です。

# 現在の時刻の表示：
# datetime ライブラリを使用して、現在の時刻を表示します。

# ファイルのダウンロードと読み込み：
# s3_bucket.download_file(xxx)：指定されたキー xxx に対応するファイルをS3からダウンロードします。
# pd.read_csv(yyy)：ダウンロードしたファイルをPandasデータフレームに読み込みます。ここで、yyy はダウンロードしたファイルのローカルパスを指定します。

# 例外処理：
# ファイルのダウンロードや読み込みに関するエラーが発生した場合、例外をキャッチしてエラーメッセージを表示します。

# 最終的に、df_campaign_master というPandasデータフレームにキャンペーンマスターデータが読み込まれ、このデータを返します。この関数を呼び出すことで、S3からデータを取得して分析や処理に使用できます。
