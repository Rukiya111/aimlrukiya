import pandas as pd
import numpy as np

s1=pd.Series([1,2,3,4,5,6])
s2=pd.Series([2,5,7,8,6,1])

union=pd.Series(np.union1d(s1,s2))
print("\n Union of two series \n ",union)

intersect=pd.Series(np.intersect1d(s1,s2))
print("\n Intersection of two Series \n",intersect)

notcomm=union[~union.isin(intersect)]
print("\n Elements not common in both series \n",notcomm)
