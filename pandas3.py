import pandas as pd
import numpy  as np
datas=pd.date_range("20170609",periods=6)
df=pd.DataFrame(np.random.randn(6,6),index=datas,columns=list("ABCDEF"))


# loc only row and column name to slice
# but iloc can use row number and colums number
print(df.iloc[:,:])
print("***********************")
print(df.iloc[0:2,0:2])

# we can catch only one value use iloc but iat is faster
print(df.iloc[1,2])

print (df.iat[1,2])