def make_dataset_F1(df):
    df['f'] = df['f'].replace(1, 0)
    df['f'] = df['f'].mask(df['f']>1, 1)
    df.rename(columns={'f':'target'}, inplace=True)
    return df.drop(columns=['date', 'user_id'])

def make_dataset_F2(df):
    df = horizontal_arrange(df)
    df['f'] = df['f'].replace(2, 0)
    df['f'] = df['f'].replace(3, 1)
    df.rename(columns={'f':'target'}, inplace=True)
    return df.drop(columns=['user_id'])

def main():
    df_label = labeling()
    df_f1 = make_dataset_F1(df_label.copy())
    df_f2 = make_dataset_F2(df_label.copy())
    df_f1 = default_screening(df_f1)
    df_f2 = default_screening(df_f2)
    df_f1.to_csv('yyy.csv', index=False)
    df_f2.to_csv('zzz.csv', index=False)
    gc.collect()

if __name__=='__main__':
    main()

# このPythonコードは、いくつかのデータ処理関数を使用してデータセットを作成し、それをCSVファイルに保存するプログラムの例です。以下に、各ステップの概要と関数の役割を説明します。
# labeling() 関数:
# デフォルトのデータセットファイルを読み込み、データを前処理およびラベリングします。
# 特定の条件に基づいて 'cum' 列を追加し、 'date' 列を日付に変換します。
# ラベリングおよび前処理が完了したデータフレーム df_label を返します。

# make_dataset_F1() および make_dataset_F2() 関数:
# df_label のコピーを受け取り、それに基づいて特定のデータセット（F1またはF2）を生成します。これには、データの変換や特定の列の選択が含まれます。

# default_screening() 関数:
# データフレームに対して条件を適用し、特定の列の値を変更または削除します。
# threshold パラメーターを使用して、条件を満たす行の選択基準を調整できます。

# データセットのCSVファイルへの保存:
# df_f1 および df_f2 データフレームをCSVファイルに保存します。
# ファイルの保存先は 'yyy.csv' および 'zzz.csv' です。

# gc.collect():
# メモリのガベージコレクションをトリガーし、不要なメモリを解放します。

# main() 関数:
# メイン関数で、上記のステップを順番に実行します。
# プログラムの実行は if __name__=='__main__': ブロック内で行われます。これにより、モジュールが他のスクリプトからインポートされた場合に main() 関数が実行されないようになります。
# このプログラムは、データ処理とデータセットの生成に関連するタスクを自動化するために使用できる一般的なデータパイプラインの例です。データの前処理、ラベリング、データセットの生成、およびデータの保存が効率的に実行されます。




