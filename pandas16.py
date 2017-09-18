# 添加趋势线
import pandas as pd
import numpy  as np
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt

data=pd.DataFrame({"A":[1,2,3,4],
	                "B":[5,6,7,8],
	               })
print(data)

lm=ols("B~A",data).fit()

plt.plot(data.A,lm.fittedvalues,"r",linewidth=2)
plt.show()

