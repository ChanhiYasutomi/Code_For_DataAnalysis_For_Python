# ROC曲線
plt.figure(figsize = (10, 10))
plt.title('ROC curve', fontsize = 22)
plt.plot(fpr, tpr, label='ROC curve (area = %.4f)'%auc, color = color0)
plt.plot([0, 1], [0, 1], '--', color = color_black, alpha = 0.5)
plt.xlabel('False Positive Rate', fontsize = 18)
plt.ylabel('True Positive Rate', fontsize = 18)
plt.xticks(np.arange(0, 1.1, 0.1))
plt.yticks(np.arange(0, 1.1, 0.1))
plt.legend(fontsize=20)
plt.grid(alpha=0.5)
plt.show()

# このコードは、ROC曲線をプロットして可視化するためのMatplotlibを使用しています。以下は、コードの主要な部分とその役割の説明です：

# plt.figure(figsize=(10, 10)):
# 新しい図（プロット領域）を作成し、そのサイズを設定しています。

# plt.title('ROC curve', fontsize=22):
# 図のタイトルを設定しています。タイトルは「ROC curve」と表示されます。

# plt.plot(fpr, tpr, label='ROC curve (area = %.4f)' % auc, color=color0):
# ROC曲線をプロットしています。
# fpr（False Positive Rate）とtpr（True Positive Rate）のデータを使用しています。
# label を使用して、ラベルとAUC（曲線下の面積）の値を表示します。

# plt.plot([0, 1], [0, 1], '--', color=color_black, alpha=0.5):
# 対角線（ランダムな分類の場合の曲線）をプロットしています。
# -- は破線を意味し、color と alpha は色と透明度を設定します。

# plt.xlabel('False Positive Rate', fontsize=18) と plt.ylabel('True Positive Rate', fontsize=18):
# x軸とy軸のラベルを設定しています。

# plt.xticks(np.arange(0, 1.1, 0.1)) と plt.yticks(np.arange(0, 1.1, 0.1)):
# x軸とy軸の目盛りを設定しています。0から1まで、0.1刻みで目盛りが表示されます。

# plt.legend(fontsize=20):
# 凡例を表示します。凡例にはROC曲線の面積（AUC）が表示されます。

# plt.grid(alpha=0.5):
# グリッド線を表示します。alpha はグリッド線の透明度を設定します。

# plt.show():
# プロットを表示します。

# このコードは、ROC曲線を視覚化し、モデルの性能を評価するために使用されます。ROC曲線は、二項分類モデルの性能を評価するための一般的な方法の一つで、AUCの値が高いほどモデルの性能が良いことを示します。
