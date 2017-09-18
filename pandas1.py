import numpy as np 
import pandas as pd

dates=pd.date_range("20140617",periods=6)
print(dates)

df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=["1","2","3","4"])
print(df)

#create matrix 6 row and 4 columns
print(np.random.randn(6,4))
print("********new*****")

#6 row datas
df2=pd.DataFrame({"S":np.random.randn(6)})
print(df2)

#series is one dimensional array
df3=pd.DataFrame({"A":pd.Timestamp("20130729"),"B":pd.Series(1,index=list(range(4)))})


print ("df3","\n",df3)


#if datas is less than index will raise erro
# df4=pd.DataFrame([1,2],index=range(3))
# print("df4","\n",df4)
# 

print(df3.dtypes)

#you can see head N row and it's before all
print(df3.head(2))

#you can see last row

print(df3.tail(2))

# you can see the index 
print (df3.index)

# you can see columns 
print (df3.columns)
# you can see data only
print (df3.values)

# you can see describe: all columns mean() ,std() and so and
print (df3.describe())

# you can transposition
print(df.T)