import pandas as pd
import numpy as np

s = pd.Series([1,3,5,6,8])

print(s)

dates = pd.date_range('2013-01-03', periods=6)

print(dates)

# df는 테이블
df = pd.DataFrame(np.random.rand(6,4), index=dates, columns=['A','B','C','D'])
print(df)

print(df.head(3))

print(df.index)

print(df.columns)

print(df.values)

print(df.describe())

print(df.sort_values(by ='B', ascending = False)) # 오름차순
print(df.sort_values(by ='B', ascending = True)) # 내림차순

print(df['A']) # 열 가져오기

print(df[0:3]) # 행 가져오기


