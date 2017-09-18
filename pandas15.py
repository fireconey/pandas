# 图形
import pandas as pd
import numpy  as np

data=pd.DataFrame({"A":[1,2,3,4],
	"B":[5,4,7,8],
	 "C":[9,10,11,12]})
print(data)

# alpha 是点的透明度
plt=data.plot(kind="scatter",x="A",y="B",alpha=0.1)
dat=plt.get_figure()
dat.savefig("D:\\plot.png")

