# 乱数シードの固定
seed_value = 0

# 1. pythonのシード固定
import os
os.environ['PYTHONHASHSEED']=str(seed_value)
 
# 2. randomのシード固定
import random
random.seed(seed_value)
 
# 3. Numpyのシード固定
import numpy as np
np.random.seed(seed_value)

# このコードは、Pythonの乱数生成器において再現性を持たせるために、シード（乱数の初期値）を固定するための方法です。シードを固定することにより、同じコードを実行しても乱数が同じ順序で生成されるため、結果が再現可能となります。

# 具体的な説明は以下の通りです：
# os.environ['PYTHONHASHSEED']=str(seed_value): Pythonのハッシュ関数にもシードを適用します。これは特にDjangoなどの一部のライブラリで必要な場合があります。
# import randomとrandom.seed(seed_value): Pythonの標準ライブラリであるrandomモジュールのシードを固定します。これにより、randomモジュールを使用するランダムな操作も再現可能になります。
# import numpy as npとnp.random.seed(seed_value): NumPyの乱数生成器にシードを適用します。NumPyは科学計算やデータ分析で広く使用されるため、データのシャッフルや乱数生成に影響を与えます。

# これらのステップを実行することで、コード内で発生する乱数が固定され、再現性が確保されます。同じシード値を使用してコードを再実行すると、同じ乱数が生成されるため、結果が一貫して再現されることになります。
