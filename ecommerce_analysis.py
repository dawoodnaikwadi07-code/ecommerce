import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
Categories =pd.read_csv("Categories.csv")
Customers = pd.read_csv("Customers.csv")
Employees = pd.read_csv("Employees.csv")
OrderDetails = pd.read_csv("OrderDetails.csv")
Orders = pd.read_csv("Orders.csv")
Products = pd.read_csv("Products.csv")
print(Categories.head())
print(Customers.head())
print(Employees.head())
print(OrderDetails.head())
print(Orders.head())
print(Products.head())
print("Categories:",Categories.shape)
print("Customers:",Customers.shape)
print("Employees:",Employees.shape)
print("OrderDetails:",OrderDetails.shape)
print("Orders:",Orders.shape)
print("Products:",Products.shape)
Categories.info()
Customers.info()
Employees.info()
OrderDetails.info()
Orders.info()
Products.info()
print(Categories.isnull().sum())
print(Customers.isnull().sum())
print(Employees.isnull().sum())
print(OrderDetails.isnull().sum())
print(Orders.isnull().sum())
print(Products.isnull().sum())
print(Categories.duplicated().sum())
print(Customers.duplicated().sum())
print(Employees.duplicated().sum())
print(OrderDetails.duplicated().sum())
print(Orders.duplicated().sum())
print(Products.duplicated().sum())
print(Categories.dtypes)
print(Customers.dtypes)
print(Employees.dtypes)
print(OrderDetails.dtypes)
print(Orders.dtypes)
print(Products.dtypes)
Customers["JoinDate"] = pd.to_datetime(Customers["JoinDate"])
print(Customers.dtypes)
Orders["OrderDate"] = pd.to_datetime(Orders["OrderDate"])
print(Orders.dtypes)
print(Categories["CategoryName"].unique())
print(Orders["PaymentMethod"].unique())
print(Customers["City"].unique())
print(Categories.describe())
print(Customers.describe())
print(Employees.describe())
print(OrderDetails.describe())
print(Orders.describe())
print(Products.describe())


Total_Sales = (OrderDetails["Quantity"]*OrderDetails["UnitPrice"]).sum()
print("Total Sales:",Total_Sales)

Total_Orders = Orders["OrderID"].nunique()
print("Total orders:",Total_Orders)

Total_Customers = Customers["CustomerID"].nunique()
print("Total Customers:",Total_Customers)

Total_Products = Products["ProductID"].nunique()
print("Total Products:",Total_Products)

Total_Employees =Employees["EmployeeID"].nunique()
print("Total_Employees:",Total_Employees)

Average_Order_Value = Total_Sales/Total_Orders
print("Average Order Value:",Average_Order_Value)

Quantity_Sold = OrderDetails["Quantity"].sum()
print("Total Quantity Sold:",Quantity_Sold)

print(OrderDetails.groupby("ProductID")["Quantity"].sum().sort_values(ascending = False).head())

Customer_Orders = pd.merge(
    Customers,
    Orders,
    on = "CustomerID",
    how = "inner"
)
print(Customer_Orders.head())

Orders_Details = pd.merge (
    Orders,
    OrderDetails,
    on = "OrderID",
    how = "inner"
)
print(Orders_Details.head())

Product_Sales = pd.merge(
    OrderDetails,
    Products,
    on = "ProductID",
    how = "inner"
)
print(Product_Sales.head())


Product_category = pd.merge(
    Products,
    Categories,
    on = "CategoryID",
    how = "inner"
)
print(Product_category.head())

Employee_Orders = pd.merge(
    Employees,
    Orders,
    on = "EmployeeID",
    how = "inner"
)
print(Employee_Orders.head())


Master_Data = pd.merge (
    Orders_Details,
    Products,
    on = "ProductID",
    how = "left"
)
Master_Data = pd.merge(
    Master_Data,
    Categories,
    on = "CategoryID",
    how = "left"
)
Master_Data  = pd.merge(
    Master_Data,
    Employees,
    on = "EmployeeID",
    how = "left"
)
Master_Data = pd.merge(
    Master_Data,
    Customers,
    on = "CustomerID",
    how = "left"
)

print(Master_Data.head())

Master_Data.to_csv("Master_Data_Final.csv",index = False)
print("Master Data Saved Successfully")

Master_Data["Revenue"]=Master_Data["Quantity"]*Master_Data["UnitPrice"]*(1-Master_Data["Discount"])
print("Total Revenue")
print(Master_Data["Revenue"].sum())

print("Total Orders")
print(Master_Data["OrderID"].nunique())

print("Total Customers")
print(Master_Data["CustomerID"].nunique())

print("Total Employees")
print(Master_Data["EmployeeID"].nunique())


Monthly_Revenue = Master_Data.groupby("OrderDate")["Revenue"].sum().reset_index()
print(Monthly_Revenue.head())

Top_Products = Master_Data.groupby("ProductName",as_index=False)["Revenue"].sum().sort_values(by = "Revenue",ascending = False)
print(Top_Products)


Top_Customers = Master_Data.groupby("CustomerID",as_index=False)["Revenue"].sum().sort_values(by = "Revenue",ascending=False)
print(Top_Customers)

Category_Revenue = Master_Data.groupby("CategoryName",as_index=False)["Revenue"].sum().sort_values(by="Revenue",ascending=False)
print(Category_Revenue)

Brand_Revenue = Master_Data.groupby("Brand")["Revenue"].sum().sort_values(ascending=False).reset_index()
print(Brand_Revenue)

Employee_Performance = Master_Data.groupby("EmployeeName")["Revenue"].sum().sort_values(ascending=False).reset_index()
print(Employee_Performance)

City_Revenue = Master_Data.groupby("City")["Revenue"].sum().sort_values(ascending=False).reset_index()
print(City_Revenue)


import matplotlib.pyplot as plt
Monthly_Revenue.plot(
    x = "OrderDate",
    y = "Revenue",
    kind = "line",
    figsize = (10,5),
    title = "Monthly Revenue Trend"
)
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.savefig("Monthly_Revenue.png")
plt.show()

Top_Products = (Master_Data.groupby("ProductName",as_index=False)["Revenue"].sum().sort_values(by = "Revenue",ascending = False).head(10))
print(Top_Products)
plt.figure(figsize=(12,6))
plt.bar(Top_Products["ProductName"],Top_Products["Revenue"])
plt.title("Top Products by Revenue")
plt.xlabel("ProductName")
plt.ylabel("Revenue")
plt.xticks(rotation = 45)
plt.tight_layout()
plt.savefig("Top_Products.png")
plt.show()

Category_Revenue = Master_Data.groupby("CategoryName",as_index=False)["Revenue"].sum().sort_values(by="Revenue",ascending=False)
print(Category_Revenue)
plt.figure(figsize = (10,6))
plt.bar(Category_Revenue["CategoryName"],Category_Revenue["Revenue"])
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation = 30)
plt.grid(axis = "y")
plt.savefig("Category_Revenue.png")
plt.show()


Brand_Revenue = Master_Data.groupby("Brand")["Revenue"].sum().sort_values(ascending=False).reset_index()
print(Brand_Revenue)
plt.figure(figsize = (10,6))
plt.bar(Brand_Revenue["Brand"],
        Brand_Revenue["Revenue"])
plt.title("Revenue by Brand")
plt.xlabel("Brand")
plt.ylabel("Revenue")
plt.xticks(rotation = 45)
plt.tight_layout()
plt.savefig("Brand_Revenue.png")
plt.show()

Customer_distribution = (Master_Data.groupby("City")["CustomerID"].nunique())
plt.figure(figsize=(8,8))
plt.pie(Customer_distribution,
labels = Customer_distribution.index,autopct = "%1.1f%%",startangle=90)
plt.title("Customer Distribution by City")
plt.savefig("Customer_Distribution.png")
plt.show()

import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
plt.hist(Master_Data["Revenue"],bins = 20,edgecolor = "black")
plt.title("Revenue Distribution")
plt.xlabel("Revenue")
plt.ylabel("Frequency")
plt.grid(axis = "y")
plt.tight_layout()
plt.savefig("Revenue_Histogram.png")
plt.show()

Master_Data_Final = pd.read_csv("Master_Data_Final.csv")
Master_Data_Final.columns

