import pandas as pd


a=pd.Series([1,2,3],index=['a','b','c'])

print(a)

data =[['Alex',20],['Bob',30],['Clark',40]]
df=pd.DataFrame(data,columns=['Name','Age'],index=['a','b','c'])
print(df)

d={'one' : pd.Series([1,2,3],index=['a','b','c']), 'two' : pd.Series([1,2,3,4],index=['a','b','c','d'])}
print(pd.DataFrame(d))
df=pd.DataFrame(d)
df['three']=pd.Series([10,20,30],index=['a','b','c'])
print(df)
df['four']=df['one']+df['two']
print(df)