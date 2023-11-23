# isupper() メソッドは、文字列内の文字が全て大文字である場合に True を返し、それ以外の場合には False を返します。以下に isupper() の具体例を示します：
# isupper() メソッドの具体例

# 大文字だけからなる文字列
uppercase_string = "HELLO"

# 大文字と小文字が混在する文字列
mixed_case_string = "Hello World"

# isupper() を使用して各文字列が全て大文字かどうかを判定
result_uppercase = uppercase_string.isupper()
result_mixed_case = mixed_case_string.isupper()

# 結果を表示
print(f'文字列 "{uppercase_string}" は全て大文字か？ {result_uppercase}')
print(f'文字列 "{mixed_case_string}" は全て大文字か？ {result_mixed_case}')

# 出力:
# 文字列 "HELLO" は全て大文字か？ True
# 文字列 "Hello World" は全て大文字か？ False

# isupper() メソッドは、文字列全体が大文字の場合に True を返し、それ以外の場合に False を返します。このメソッドは、文字列が大文字だけから構成されているかどうかを簡単に確認するのに役立ちます。
