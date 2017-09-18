import pandas as pd
import numpy  as np
datas=pd.date_range("20170609",periods=6)
df=pd.DataFrame(np.random.randn(6,6),index=datas,columns=list("ABCDEF"))

print(df)
# if you want to check A column datas
print(df["A"])
# clice only row data and can't use to column
print(df[1:3])
# we can use index to select row
print(df["2017-06-10":"2017-06-11"])
# **********************************************
# we only use column name select column and 
# only user clice to select row

# loc function() can slice row and column
print(df.loc[datas[0]])#must use datas ,it to show 0row datas
print("***************")
print(df.loc["20170609":"20170611","A":"B"])    #row  only use row name and column name

# only catch one value
print("***************")
print(df.at[datas[0],"A"])