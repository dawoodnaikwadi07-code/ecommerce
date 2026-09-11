create database ecommerce1;
use ecommerce1;
create table customers (
customerID int primary key,
firstname varchar(50),
lastname varchar(50),
age int,
city varchar (20),
state varchar (20),
joindate date );

create table categories(
categoryID int primary key,
categoryname varchar(50));


create table products (
productID int primary key,
productname varchar (100),
categoryID int,
brand varchar (50),
price decimal (10,2),
stockquantity int,
foreign key (categoryID)
references categories(categoryID));

create table employees (
employeeID int primary key,
employeename varchar (100),
department varchar (50),
salary decimal (10,2));

create table orders(
orderID int primary key,
customerID int,
employeeID int,
OrderDate date ,
paymentmethod varchar (20),
foreign key (customerID)
references customers(customerID),
foreign key (employeeID)
references employees(employeeID));

create table orderdetails (
orderdetailID int primary key,
orderID int ,
productID int, 
Quantity int,
unitprice decimal(10,2),
discount decimal(5,2),
foreign key (orderID)
REFERENCES orders(orderID),
foreign key (productID)
REFERENCES products(productID));

use ecommerce1;
select * from orderdetails;
select * from customers;
select * from products;
select * from categories;
select * from employees;
select * from orders;

-- Total Number of customers--
select count(*) as Total_customers from customers;

-- Total number of products --
select count(*) as Total_products from products;

-- Total number of orders --
select count(*) as Total_orders from orders;

-- Total Inventory Available --
select sum(stockquantity) as Total_stock from products;

-- average product price --
select avg(price) as Average_price from products;

-- Total sales of company --
select sum(quantity * unitprice) as Total_sales
from orderdetails;

-- Average Order Value --
select avg(quantity * unitprice) as Average_order_value
from orderdetails;

-- Top 5 most expensive products--
select productname,price from products
order by price desc
limit 5;

-- customer Wise total spending --
select customers.customerID,customers.firstname,customers.lastname,sum(orderdetails.quantity*orderdetails.unitprice) as Total_spending
from customers inner join orders on
customers.customerID = orders.customerID
inner join orderdetails on 
orders.orderID = orderdetails.orderID
GROUP BY customers.customerID,customers.firstname,customers.lastname
order by Total_spending desc;

-- Top 5 best selling products --
select products.productname,sum(orderdetails.quantity) as Total_Quantity_sold
from products inner join orderdetails on 
products.productID = orderdetails.productID
GROUP BY products.productname
order by Total_quantity_sold desc
limit 5;

-- sales by category --
select categories.categoryname,sum(orderdetails.quantity*orderdetails.unitprice) as Total_sales
from categories inner join products on 
categories.categoryID = products.productID
inner join orderdetails on 
products.productID = orderdetails.productID
group by categories.categoryname
order by Total_sales desc;

-- Monthly sales report --
select month(orders.orderdate) as month,year(orders.orderdate) as year,sum(orderdetails.quantity*orderdetails.unitprice) as monthly_sales
from orders inner join orderdetails on 
orders.orderID = orderdetails.orderID
group by year(orders.orderdate),month(orders.orderdate)
order by year,month;

-- products with low stock --
select productname, stockquantity from products 
where stockquantity < 20;

-- Employee performance --
select employees.employeename,count(orders.orderID) as Total_orders
from orders inner join employees on 
employees.employeeID = orders.employeeID
GROUP BY employees.employeename
order by Total_orders desc;

-- Highest revenue product --
select products.productname,sum(orderdetails.quantity*orderdetails.unitprice) as Revenue
from products inner join orderdetails on
products.productID = orderdetails.productID
group by products.productname
order by Revenue desc
limit 1;

--
create view Highest_Revenue_product as 
select products.productname,sum(orderdetails.quantity*orderdetails.unitprice) as Revenue
from products inner join orderdetails on
products.productID = orderdetails.productID
group by products.productname
order by Revenue desc
limit 1;

