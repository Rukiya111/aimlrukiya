import pandas as pd
import numpy as np

a=np.array([1,2,3,4,5,6])
s=pd.Series(a)
print(a)
print(s)

a=pd.Series(4,index=[0,1,2,3])

print(a)

i=pd.Index([2,1,1,np.nan,3])
print(i.value_counts())


           
