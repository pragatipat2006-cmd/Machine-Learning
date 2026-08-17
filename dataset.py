import pandas as pd
df = pd.read_csv("Exp1/diabetes.csv")
print(df)

# Data filtering and cleaning
df_drop = df.drop('blood_glucose_level', axis=1)
print(df)

print(df[df['age'] > 76])

print(df_drop.sort_values(by='age'))

# Handling non numerical data (encoding) -> One - Hot Encoding
df_OHE = pd.get_dummies(df, columns=['gender'], dtype=int)
print(df_OHE)

# Handling Missing Data
df_null = df_OHE.isnull()
print(df_null)
