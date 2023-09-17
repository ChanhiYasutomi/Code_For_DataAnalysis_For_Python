def get_data(
    bucket_name='xxx', 
    key='yyy.zip'):
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket_name, Key=key)
    file_content = response['Body'].read()
    zip_file = ZipFile(io.BytesIO(file_content))
    return pd.read_csv(zip_file.open(zip_file.infolist()[0]))

# 提供されたコードは、Amazon S3からZIPファイル内のCSVデータを取得し、それをPandasのデータフレームに読み込むための関数です。以下に関数内の主要なステップと役割を説明します：
# bucket_name と key パラメーター:
# bucket_name パラメーターは、データが格納されているAmazon S3バケットの名前を指定します。
# key パラメーターは、取得したいZIPファイルのS3キー（ファイルのパス）を指定します。

# boto3 クライアントの初期化:
# boto3 ライブラリを使用して、Amazon S3サービスへの接続を確立します。

# S3オブジェクトの取得:
# s3.get_object() メソッドを使用して、指定したバケットから指定したキーのオブジェクトを取得します。

# ファイル内容の読み込み:
# 取得したオブジェクトからZIPファイルの内容をバイト列として読み込みます。

# バイト列をZipファイルに変換:
# 読み込んだバイト列を io.BytesIO を使用してZipファイルに変換します。

# Zipファイル内のCSVファイルの読み込み:
# ZipFile クラスを使用して、Zipファイル内のCSVファイルを取得し、それをPandasのデータフレームに読み込みます。
# zip_file.infolist()[0] はZipファイル内の最初のファイルを指定しています。必要に応じて他のファイルを指定できます。

# データフレームの返却:
# 読み込んだCSVデータをPandasのデータフレームとして返却します。
      
# この関数を呼び出すことで、指定したS3バケットから指定したZIPファイル内のCSVデータを取得し、それをデータフレームとして利用できます。データの前処理や分析に使用するのに便利です。
# ただし、bucket_name と key パラメーターには、実際のS3バケットとファイルのパスを指定する必要があります。
