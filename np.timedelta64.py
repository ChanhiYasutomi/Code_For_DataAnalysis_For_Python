# np.timedelta64は、NumPyで時間差を表現するためのデータ型です。timedelta64は時間の差分や経過時間を表現するのに便利で、日単位や秒単位など様々な時間単位で指定することができます。
# 以下は、np.timedelta64(1, 'D')の具体的な例です。
import numpy as np

# 1日分の時間差を表現する
one_day = np.timedelta64(1, 'D')

# 例: 今から1日後はいつか
current_time = np.datetime64('2023-01-01')
one_day_later = current_time + one_day

display(f"現在の日時: {current_time}")
display(f"1日後の日時: {one_day_later}")

# この例では、np.timedelta64(1, 'D')を使用して1日分の時間差を表現し、それを現在の日時に足しています。np.timedelta64は時間単位を指定する引数を受け取り、'D'は日単位であることを示しています。
# なお、np.datetime64は日時を表現するためのデータ型であり、np.timedelta64と一緒に使用することで日時の計算が行えます。
