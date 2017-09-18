# read current path
import os
print(os.getcwd())
# pd.read_csv(, encoding) use to while you use other fomat to save file
# and at time you want to read it right

import pandas as pd
data=pd.read_csv("C:\\Users\\TH\\Desktop\\ok.csv",encoding="gbk")
print (data)


# count value .we only use one specipotion array to count()
print (data["语文"].value_counts())
df=data["语文"].value_counts()
# pandas has plot function

# kind is type will to  painting 
plt=df.plot(kind="bar").get_figure()
plt.savefig("D:\\plot.png")


# 
print(data[data.数学>56])

