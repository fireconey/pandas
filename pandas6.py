# use groupby
import numpy as np
import pandas as pd
data=pd.DataFrame({
	"one1":["one","three","two","one","two","one"],
	"two1":[1,2,3,4,5,6],
	"three1":[7,8,9,10,11,12]
	})
print (data)

# groupby is specify on what to group ,相同的放在一组如
# 有多个不同行的one ，多个one就放在一组。
# firt（）表示的是每组的第一行的数字
group=data.groupby(data["one1"])
print(dict(list(group)))

print(group.first())