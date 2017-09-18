#处理NAN数据
import pandas as pd
import numpy  as np

data=pd.DataFrame({"A":[1,2,3,4],
	"B":[5,np.NaN,np.NaN,8],
	 "C":[9,10,11,12]})
print(data)

# all use previous data fill
# data=data.fillna(method="pad")
# print(data)

# all use behind data fill,but "limit" can limit how
# many data to fill 
data=data.fillna(method="bfill",limit=1)
print(data)

# use any one to fill
# data=data.fillna("th")
# print(data)


# dropna
d=data.dropna(axis=1)
print(d,"*****")
print(data)

# insert valu to fill
# ins=data.interpolate()
# print(ins)

# use index means to insert value to fill
op=data.interpolate(method="values")
print(op,"**********")