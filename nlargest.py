# nlargest メソッドは、Pandasのデータフレームやシリーズから最大の要素を持つ行または要素を取得するためのメソッドです。以下に、具体的な例を挙げて説明します。
import pandas as pd

# サンプルのデータフレームを作成
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
        'Age': [25, 30, 35, 40, 22],
        'Salary': [50000, 60000, 75000, 90000, 48000]}

df = pd.DataFrame(data)

# 'Salary' 列が最大の行を取得（デフォルトでは1行）
max_salary_row = df.nlargest(1, 'Salary')

print("DataFrame:")
display(df)
print("\nRow with the largest salary:")
display(max_salary_row)

# この例では、'Salary' 列が最大の行を取得しています。nlargest メソッドの第一引数には取得する行数を指定し、第二引数には最大値を調べる対象の列名を指定します。デフォルトでは最大の行が1行返されます。
# 上記のコードの出力は以下のようになります：
# DataFrame:
#       Name  Age  Salary
# 0    Alice   25   50000
# 1      Bob   30   60000
# 2  Charlie   35   75000
# 3    David   40   90000
# 4     Emma   22   48000

#     Name  Age  Salary
# 3  David   40   90000
# この場合、'Salary' 列が最大の行は David で、その情報が含まれた新しいデータフレームが返されます。
