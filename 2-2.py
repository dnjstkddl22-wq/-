import pandas as pd

score = pd.DataFrame([[85, 86, 40, 95],
                     [85, 86, 40, 95],
                     [85, 86, 40, 95]]),


print(score)  
print(type(score)) 

print(score.index)
print(score.columns)

print(score.iloc[1, 2])
