# 混合索引
import numpy as np
import pandas as pd
import random as rd
color=[]
foods=[]
for i  in range(0,10):
	color.append(rd.choice(["red","blue"]))
	foods.append(rd.choice(["eggs","ham"]))
print(color)
print(foods)

index=pd.MultiIndex.from_arrays([color,foods],names=["color","food"])
data=pd.DataFrame(np.random.randn(10,3),index=index,columns=list("ABC"))
print(data[1:3])



gt=data.groupby("color")
print(list(gt))
print("***********************")
# 删除所有索引,那些索引数据还在，只是不做为索引了。
# 使用ilevel_0表示第一行。level=0表示第一个索引
data.index.names=[None,None]
print(data)