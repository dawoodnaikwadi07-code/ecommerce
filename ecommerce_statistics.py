import pandas as pd
Master_Data_Final = pd.read_csv("Master_Data_Final.csv")
print(Master_Data_Final.columns)
print(Master_Data_Final.info())
print(Master_Data_Final.describe())
print(Master_Data_Final.select_dtypes(include = "number").columns)
numeric_cols = ["Quantity","UnitPrice","Discount","Price","StockQuantity","Salary","Age"]
print(Master_Data_Final[numeric_cols].describe())

for col in numeric_cols:
    print(col,"mean =",Master_Data_Final[col].mean())
    print(col,"mean =",Master_Data_Final[col].median())
    print(col,"mean =",Master_Data_Final[col].mode().tolist())

for col in numeric_cols:
    Maximum = Master_Data_Final[col].max()
    Minimum = Master_Data_Final[col].min()
    Range_Value = Maximum - Minimum

    print("\n",col)
    print("Maximum:",Maximum)
    print("Minimum:",Minimum)
    print("Range:",Range_Value)

for col in numeric_cols:
    print(col,"Variance:",Master_Data_Final[col].var())

for col in numeric_cols:
    print(col,"Standard Deviation:",Master_Data_Final[col].std())

for col in numeric_cols:
    Q1 = Master_Data_Final[col].quantile(0.25)
    Q2 = Master_Data_Final[col].quantile(0.50)
    Q3 = Master_Data_Final[col].quantile(0.75)
    print("\n",col)
    print("Q1:",Q1)
    print("Q2:",Q2)
    print("Q3:",Q3)

for col in numeric_cols:
    Q1 = Master_Data_Final[col].quantile(0.25)
    Q3 = Master_Data_Final[col].quantile(0.75)
    IQR = Q3-Q1
    print("IQR:",IQR)


for col in numeric_cols:
    Q1 = Master_Data_Final[col].quantile(0.25)
    Q3 = Master_Data_Final[col].quantile(0.75)
    IQR = Q3-Q1
    lower = Q1 - 1.5 *IQR
    Upper = Q3 + 1.5 * IQR
    Outliers = Master_Data_Final[(Master_Data_Final[col]<lower)|(Master_Data_Final[col]>Upper)]
    print("\n",col)
    print("Lower Bound:",lower)
    print("Upper Bound:",Upper)
    print("Number of Outliers:",len(Outliers))

for col in numeric_cols:
    print(col,"skewness:",Master_Data_Final[col].skew())

correlation = Master_Data_Final[numeric_cols].corr()
print(correlation)

covariance = Master_Data_Final[numeric_cols].cov()
print(covariance)