# 一列数据需要转换为以1为标准差以0为平均数的标准分数
import pandas as pd  #data  deal
import numpy as np   #data  caculate
data=pd.DataFrame({"A":[1,2,3,4],
					"B":[0.5,0.6,0.27,0.5]
					},index=[9,10,11,12])

print(data.index)

# # transform()
key=lambda x:x.index()
print(key)
zscore=lambda x:(x-x.mean())/x.std()
tr=data.groupby(key).transform(zscore)
print(tr)