# enumerate() は、Pythonのビルトイン関数で、イテラブル（リスト、タプル、文字列など）内の要素とそれらのインデックスを同時に取得するのに役立ちます。具体的な例を示します。

# サンプルリストを作成
fruits = ['apple', 'banana', 'cherry']

# enumerate() を使ってリスト内の要素とインデックスを取得
for index, fruit in enumerate(fruits):
    print(f'Index: {index}, Fruit: {fruit}')
  
# このコードでは、enumerate() を使用して fruits リスト内の各要素とそのインデックスを取得しています。ループ内で index と fruit という変数を使って、要素とそのインデックスを表示しています。

# 出力結果は次のようになります：

# Index: 0, Fruit: apple
# Index: 1, Fruit: banana
# Index: 2, Fruit: cherry

# このように、enumerate() を使用することで、イテラブル内の要素とそれらのインデックスを効果的に処理できます。これはループ処理や特定の要素にアクセスする際に便利です。
