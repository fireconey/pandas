# use aggregate and agg

import pandas as pd  #data  deal
import numpy as np   #data  caculate
data=pd.DataFrame({"A":[1,2,3,4],
					"B":[5,6,7,8]
					},index=[9,10,11,12])
print(data)
# can make index to data
print(data.reset_index())

#aggregate can use only one function
print (data.aggregate(np.sum))

# size()函数
print (data.groupby("A").size())

# deiscrit count will show   std  means ....
print(data.describe())

