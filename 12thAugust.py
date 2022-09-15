import numpy as np
a =np.array([[1,2,3,4],[5,6,7,8]])

print(a)
a.resize(1,8)
print(a)
a.resize(2,4)
print(a)
a.resize(4,2)
print(a)
a.resize(2,2,2)

import pandas as pd


d={'Col1' : pd.Series([1,2,3,4],index=['a','b','c','e']), 'Col2' : pd.Series([4,5,6],index=['x','y','z'])}
p=pd.DataFrame(d)
p['Col1'].fillna(1,inplace=True)
p['Col2'].fillna(2,inplace=True)
p.loc['b'].at['Col1']=10
p.loc['z'].at['Col2']=20



print(p)