# 在矩阵运算中经常用到的一种操作。
# 一个矩阵或者向量减去一个常数，
# 那么通常是矩阵中的每一个元素减去这个常数，这就是广播，
# 这种简单的广播就不再举例了，
# 我们看看列或者行广播。
# 如果运算时遇到Nan 结果也为Nan
import pandas as pd
import numpy  as np
data=pd.DataFrame({"A":[1,2],
	                "B":[3,4]})
print(data)


# what row data get
row=data.ix[1]
print("***************************")
print(row)
print("***************************")
print(data-row)

print(data-1)

