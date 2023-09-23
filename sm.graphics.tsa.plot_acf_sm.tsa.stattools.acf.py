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
# acf_result(autocorrelation coefficient): 自己相関係数
# confint(confidence interval): 自己相関係数(acf_result)の95%信頼区間(alpha=0.05 -> これはデフォルトで0.05(95%信頼区間))
acf_result, confint = sm.tsa.acf(df["Average Temperature (℃)"], nlags=9, fft=False, alpha=0.05) #これがかなり使える(大事) -> 69行目以降から出力する方法を記載

# 自己相関のプロット
plt.bar(range(10), acf_result)
plt.title("Autocorrelation Plot")
plt.xlabel("Lag")
plt.ylabel("Autocorrelation")
plt.show()

# このコードでは、まずサンプルの時系列データを作成し、それを sm.tsa.acf() 関数に渡して自己相関係数を計算します。nlags パラメータは計算するラグの数を指定します。
# fft パラメータは高速フーリエ変換（Fast Fourier Transform）を使用するかどうかを制御します。alphaパラメータは信頼区間を計算するために使用され、デフォルトでは0.05（95％信頼区間）です。

# 計算された自己相関係数をプロットすると、各ラグにおける自己相関の値が表示され、データ内のパターンや周期性を示すことができます。
# 自己相関がラグ0で高い場合、データにトレンドや周期性があることを示す可能性があります。ラグ1以降の自己相関が高い場合、そのラグ数に対応する周期性が存在する可能性があります。このようなプロットを通じて、時系列データの特性を把握し、モデル化や予測に役立てることができます。



# acf_resultとconfintの部分について教えて
# acf_result は自己相関係数（Autocorrelation Coefficients）の配列です。この配列には、ラグ0から nlags までの各ラグに対する自己相関係数が含まれています。ラグ0の自己相関は必ず1です。
# ラグ1から nlags までの自己相関係数は、それぞれのラグにおける時間遅れ（時間の差分）と現在のデータとの相関を示します。この自己相関係数は、時系列データのラグ（過去の時点との関係）を調査するのに役立ちます。

# confint は信頼区間（Confidence Intervals）の配列です。この配列には、自己相関係数の各ラグに対する信頼区間が含まれています。
# 信頼区間は、自己相関係数の推定値がどの程度確実かを示します。デフォルトでは、95%信頼区間が計算されます。
# これは、自己相関係数がこの信頼区間内にある場合、その値が統計的に有意であると考えられることを意味します。信頼区間は、時系列データの統計的な性質を評価し、特定のラグが重要かどうかを判断するのに役立ちます。

# この情報を使って、自己相関係数のプロットに信頼区間を追加したり、統計的仮説検定を実施したりすることができます。信頼区間がゼロを含まない場合、対応するラグの自己相関が統計的に有意である可能性が高いことを示唆しています。



# データフレームで出力
import pandas as pd
import statsmodels.api as sm

# データを読み込むなどして適切な時系列データを用意

# 自己相関係数の計算
acf_result, confint = sm.tsa.acf(df["Average Temperature (℃)"], fft=False, nlags=400, alpha=0.05)

# 結果をデータフレームに整理
result_df = pd.DataFrame({
    "Lag": range(len(acf_result)),
    "ACF": acf_result,
    "Lower 95% CI": [lower for lower, _ in confint],
    "Upper 95% CI": [upper for _, upper in confint]
})

# 結果を表示
display(result_df)

# 出力(データフレーム)
# Lag	ACF	Lower 95% CI	Upper 95% CI
# 0	0	1.000000	1.000000	1.000000
# 1	1	-0.048649	-0.668444	0.571146
# 2	2	-0.637838	-1.259098	-0.016578
# 3	3	-0.006306	-0.842090	0.829477
# 4	4	0.404505	-0.431297	1.240306
# 5	5	0.027027	-0.880869	0.934923
# 6	6	-0.327928	-1.236133	0.580277
# 7	7	0.037838	-0.914767	0.990443
# 8	8	0.083784	-0.869398	1.036966
# 9	9	-0.032432	-0.988439	0.923574



# zipで出力
import statsmodels.api as sm

# データを読み込むなどして適切な時系列データを用意

# 自己相関係数の計算
acf_result, confint = sm.tsa.acf(df["Average Temperature (℃)"], fft=False, nlags=400, alpha=0.05)

# 結果を表示
for lag, acf, (lower, upper) in zip(range(len(acf_result)), acf_result, confint):
    print(f"Lag {lag}: ACF {acf:.6f}, 95%信頼区間 [{lower:.6f}, {upper:.6f}]")

# 出力
# Lag 0: ACF 1.000000, 95%信頼区間 [1.000000, 1.000000]
# Lag 1: ACF -0.048649, 95%信頼区間 [-0.668444, 0.571146]
# Lag 2: ACF -0.637838, 95%信頼区間 [-1.259098, -0.016578]
# Lag 3: ACF -0.006306, 95%信頼区間 [-0.842090, 0.829477]
# Lag 4: ACF 0.404505, 95%信頼区間 [-0.431297, 1.240306]
# Lag 5: ACF 0.027027, 95%信頼区間 [-0.880869, 0.934923]
# Lag 6: ACF -0.327928, 95%信頼区間 [-1.236133, 0.580277]
# Lag 7: ACF 0.037838, 95%信頼区間 [-0.914767, 0.990443]
# Lag 8: ACF 0.083784, 95%信頼区間 [-0.869398, 1.036966]
# Lag 9: ACF -0.032432, 95%信頼区間 [-0.988439, 0.923574]
