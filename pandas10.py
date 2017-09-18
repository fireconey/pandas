import pandas as pd  #data  deal
import numpy as np   #data  caculate
data=pd.DataFrame({"A":[1,2,3,4],
					"B":[0.5,0.6,0.27,0.5],
					"C":[9,10,11,12]})
print(data)

# add column
data.C=pd.Series(np.random.randn(4),index=data.index)
print(data)

# selection position to insert
data.insert(1,"E",data.C)
print(data)

# del data,we del list not attribute so not data.C
del data["C"]
print (data)


# drop will make new dataframe but not have you 
# want to del
# we del data that contain "A" letter
# in columns name or row name,

df=data.drop([0,],axis=0)
print(df)


# pop is get datas to parameter and del previous datas
key=data.pop("A")
print(data)
data.insert(2, "A", key)

print(data)
