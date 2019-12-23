import pandas as pd

df = pd.read_csv("final.csv")
df["星級"] = df["星級"].replace({"none": "0"})
df["評論數"] = df["評論數"].replace({"none": "0"})
df["星級"] = pd.to_numeric(df['星級'], errors='coerce')    # 將星級轉為float
df["評論數"] = df["評論數"].astype(int)
print(df.info())
print(df.head())
print("=============================================================")

print("評論數：", df["評論數"].describe())

df.drop(df.loc[df['星級'] < 4].index, inplace=True)
df.drop(df.loc[df['評論數'] < 76].index, inplace=True)
print(df.head())

export_csv = df.to_csv(r'C:\\Users\\王豫平\\Desktop\\學業\\商管程式設計\\final project\\FoodPanda_Data.csv')