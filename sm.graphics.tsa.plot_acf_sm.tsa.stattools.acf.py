# sm.graphics.tsa.plot_acf() は、StatsModelsライブラリを使用して時系列データの自己相関（Autocorrelation）を可視化するための関数です。
# 自己相関は、データ内の過去の観測値と現在の観測値との関連性を示します。具体的には、ラグ（Lag）と呼ばれる時間の遅れを持つ自己相関をプロットします。これにより、データ内のパターンや周期性を可視化するのに役立ちます。
# 以下に具体的な例を示します。
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# サンプルの時系列データを作成
data = {'Average Temperature (℃)': [25, 28, 30, 24, 26, 29, 31, 27, 26, 28]}
df = pd.DataFrame(data)

# 自己相関のプロット
sm.graphics.tsa.plot_acf(df["Average Temperature (℃)"], lags=9)  # lagsはラグの数を指定
plt.title("Autocorrelation Plot")
plt.xlabel("Lag")
plt.ylabel("Autocorrelation")
plt.show()

# このコードでは、まずサンプルの時系列データを作成し、それを sm.graphics.tsa.plot_acf() 関数に渡して自己相関をプロットします。lags パラメータは、表示するラグの数を指定します。上記の例では lags=9 としていますので、ラグ0からラグ9までの自己相関がプロットされます。
# プロットを解釈すると、各ラグにおける自己相関の値が表示され、データ内のパターンや周期性を示すことができます。自己相関がラグ0で高い場合、データにトレンドや周期性があることを示す可能性があります。
# ラグ1以降の自己相関が高い場合、そのラグ数に対応する周期性が存在する可能性があります。このようなプロットを通じて、時系列データの特性を把握し、モデル化や予測に役立てることができます。



# 以下でも表示できる
# sm.tsa.stattools.acf は、StatsModelsライブラリを使用して時系列データの自己相関（Autocorrelation）を計算するための関数です。
# 自己相関は、データ内の過去の観測値と現在の観測値との関連性を示します。この関数は、自己相関係数（ACF）を計算し、結果を返します。自己相関係数はラグと呼ばれる時間の遅れに対する自己相関を表します。
# 以下に具体的な例を示します。
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# サンプルの時系列データを作成
data = {'Average Temperature (℃)': [25, 28, 30, 24, 26, 29, 31, 27, 26, 28]}
df = pd.DataFrame(data)

# 自己相関を計算
# sm.tsa.stattools.acf(df["Average Temperature (℃)"],nlags=9)[9] #9番目の相関を出力
# acf_result: sm.tsa.stattools.acf(df["Average Temperature (℃)"],nlags=9)と同じ
acf_result, confint = sm.tsa.acf(df["Average Temperature (℃)"], nlags=9, fft=False, alpha=0.05)

# 自己相関のプロット
plt.bar(range(10), acf_result)
plt.title("Autocorrelation Plot")
plt.xlabel("Lag")
plt.ylabel("Autocorrelation")
plt.show()

# このコードでは、まずサンプルの時系列データを作成し、それを sm.tsa.acf() 関数に渡して自己相関係数を計算します。nlags パラメータは計算するラグの数を指定します。
# fft パラメータは高速フーリエ変換（Fast Fourier Transform）を使用するかどうかを制御します。alpha パラメータは信頼区間を計算するために使用され、デフォルトでは0.05（95％信頼区間）です。

# 計算された自己相関係数をプロットすると、各ラグにおける自己相関の値が表示され、データ内のパターンや周期性を示すことができます。
# 自己相関がラグ0で高い場合、データにトレンドや周期性があることを示す可能性があります。ラグ1以降の自己相関が高い場合、そのラグ数に対応する周期性が存在する可能性があります。このようなプロットを通じて、時系列データの特性を把握し、モデル化や予測に役立てることができます。



# acf_resultとconfintの部分について教えて
# acf_result は自己相関係数（Autocorrelation Coefficients）の配列です。この配列には、ラグ0から nlags までの各ラグに対する自己相関係数が含まれています。ラグ0の自己相関は必ず1です。
# ラグ1から nlags までの自己相関係数は、それぞれのラグにおける時間遅れ（時間の差分）と現在のデータとの相関を示します。この自己相関係数は、時系列データのラグ（過去の時点との関係）を調査するのに役立ちます。

# confint は信頼区間（Confidence Intervals）の配列です。この配列には、自己相関係数の各ラグに対する信頼区間が含まれています。
# 信頼区間は、自己相関係数の推定値がどの程度確実かを示します。デフォルトでは、95%信頼区間が計算されます。
# これは、自己相関係数がこの信頼区間内にある場合、その値が統計的に有意であると考えられることを意味します。信頼区間は、時系列データの統計的な性質を評価し、特定のラグが重要かどうかを判断するのに役立ちます。

# この情報を使って、自己相関係数のプロットに信頼区間を追加したり、統計的仮説検定を実施したりすることができます。信頼区間がゼロを含まない場合、対応するラグの自己相関が統計的に有意である可能性が高いことを示唆しています。
