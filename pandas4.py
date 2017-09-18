# we select datas 
import pandas as pd
import numpy  as np
datas=pd.date_range("20170609",periods=6)
df=pd.DataFrame(np.random.randn(6,6),index=datas,columns=list("ABCDEF"))

# it will return false or true
print(df.D>0)

# we can use above to select datas
print(df[df.D>0])

# we can select below many conditions
print(df[(df.D<0)&(df.F<0)])
# we can select only other columns by condition E,F
# first median bracket means colunm not columns so wo must
# to use list to select
print(df[["A","B"]][df.D>0])

# select specify values use isin function
atin=["0.042878"]
print(df.isin(atin))