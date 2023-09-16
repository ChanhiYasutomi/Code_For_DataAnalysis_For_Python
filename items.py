# items() メソッドは、Pythonの辞書（dictionary）で使用されるメソッドで、辞書内のキーと値のペアを取得するのに使用されます。以下に具体的な例を示します。

# サンプルの辞書を作成
student_scores = {
    'Alice': 95,
    'Bob': 88,
    'Charlie': 92,
    'David': 78
}

# items() を使って辞書内のキーと値のペアを取得
for name, score in student_scores.items():
    print(f'Name: {name}, Score: {score}')
  
# このコードでは、items() メソッドを使用して student_scores 辞書内のキーと値のペアを取得し、ループ内で name と score という変数を使ってキーと値を表示しています。

# 出力結果は次のようになります：

# Name: Alice, Score: 95
# Name: Bob, Score: 88
# Name: Charlie, Score: 92
# Name: David, Score: 78

# items() メソッドを使うことで、辞書内のすべてのキーと値に簡単にアクセスできます。これは、辞書の内容を反復処理する際に非常に便利です。
