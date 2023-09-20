# 水平バー（横向きのバー）のヒストグラムを表示するには、Matplotlibを使用して barh メソッドを使います。以下は、abc['hour'] のデータを水平バーとして表示する方法です。
import pandas as pd
import matplotlib.pyplot as plt

# 仮のデータフレームを作成
data = {'hour': [10, 14, 10, 14, 18, 18, 18]}
abc = pd.DataFrame(data)

# ヒストグラムを水平バーとしてプロット
plt.barh(abc['hour'], range(0, len(abc)))  # y軸の位置をデータに基づいて設定
plt.ylabel('Hour')
plt.xlabel('Frequency')
plt.title('Horizontal Histogram of Hour')
plt.yticks(abc['hour'])  # y軸の目盛りをデータに合わせて設定
plt.show()

# このコードでは、plt.barh を使用して水平バーのヒストグラムをプロットしています。y 軸に時間帯のデータを設定し、xlabel、ylabel、title、yticks を使用してラベル、タイトル、y軸の目盛りを設定しています。
# このコードを実行すると、時間帯に対応する水平バーのヒストグラムが表示されます。
