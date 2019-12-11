import pandas as pd
from sklearn.linear_model import LinearRegression

bike = pd.read("file")
print(bike.head())

lm = LinearRegression()

lent = bike["lent"].values.reshape(-1, 1)
pre =  bike["precipitation"].values.reshape(-1, 1)

lm.fit(pre, lent)

print("Coefficient:", lm.coef_)
print("Intercept:", lm.intercept_)
print("R square:", lm.score(pre, lent))