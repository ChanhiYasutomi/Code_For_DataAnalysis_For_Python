# random.randrangeは、指定した範囲内からランダムな整数を生成する関数です。
# この関数は、指定された範囲の最小値から最大値の手前までの整数をランダムに選択します。
# 以下は、random.randrangeの具体的な例です。

import random

# 0から9までのランダムな整数を生成
random_number = random.randrange(10)
print(f"ランダムな整数: {random_number}")

# 1から10までのランダムな整数を生成
random_number_1_to_10 = random.randrange(1, 11)
print(f"1から10までのランダムな整数: {random_number_1_to_10}")

# 0から100まで、5刻みのランダムな整数を生成
random_number_with_step = random.randrange(0, 101, 5)
print(f"0から100まで、5刻みのランダムな整数: {random_number_with_step}")

# この例では、random.randrangeを使用して異なる範囲でランダムな整数を生成しています。
# random.randrange(start, stop, step)の形式で範囲とステップを指定することができます。stopは指定された値の手前の値までが範囲に含まれます。
# なお、random.randrangeはPythonの標準ライブラリのrandomモジュールに属しています。
