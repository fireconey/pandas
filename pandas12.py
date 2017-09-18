import pandas as pd
import numpy  as np
data=pd.DataFrame({"A":["a1","b2"]})
print(data)

# 中括号是范围，小括号是正则，是要匹配
print(data.A.str.extract("(r[abd])(\d)"))