# SQL必知必会第五版练习笔记
## 第2课 检索数据
1．编写SQL语句，从Customers表中检索所有的ID（cust_id）。
```SQL
SELECT cust_id
FROM Customers;
```
2．OrderItems表包含了所有已订购的产品（有些已被订购多次）。编写SQL语句，检索并列出已订购产品（prod_id）的清单（不用列每个订单，只列出不同产品的清单）。提示：最终应该显示7行。
```SQL
SELECT DISTINCT prod_id
FROM OrderItes;
```
3．编写SQL语句，检索Customers表中所有的列，再编写另外的SELECT语句，仅检索顾客的ID。使用注释，注释掉一条SELECT语句，以便运行另一条SELECT语句。（当然，要测试这两个语句。）
```SQL
SELECT *
# SELECT cust_id
FROM Customers;
```
## 第3课 排序检索数据
1．编写SQL语句，从Customers中检索所有的顾客名称（cust_names），并按从Z到A的顺序显示结果。
```SQL
SELECT cust_names
FROM Customers
ORDER BY cust_names DESC;
```
2．编写SQL语句，从Orders表中检索顾客ID（cust_id）和订单号（order_num），并先按顾客ID对结果进行排序，再按订单日期倒序排列。
```SQL
SELECT cust_id, order_num
FROM Orders
ORDER BY cust_id, order_date DESC;
```
3．显然，我们的虚拟商店更喜欢出售比较贵的物品，而且这类物品有很多。编写SQL语句，显示OrderItems表中的数量和价格（item_price），并按数量由多到少、价格由高到低排序。
```SQL
SELECT quantity, item_price
FROM OrderItems
ORDER BY quantity DESC, item_price DESC;
```
4．下面的SQL语句有问题吗？（尝试在不运行的情况下指出。）
```SQL
SELECT vend_name,
FROM Vendors
ORDER vend_name DESC;
```
答案: There should not be a comma after vend_name (a comma is only used to separate multiple columns), and BY is missing after ORDER.
## 第4课 过滤数据
1．编写SQL语句，从Products表中检索产品ID（prod_id）和产品名称（prod_name），只返回价格为9.49美元的产品。
```SQL
SELECT prod_id, prod_name
FROM Products
WHERE prod_price = 9.49;
```
2．编写SQL语句，从Products表中检索产品ID（prod_id）和产品名称（prod_name），只返回价格为9美元或更高的产品。
```SQL
SELECT prod_id, prod_name
FROM Products
WHERE prod_price >= 9;
```
3．结合第3课和第4课编写SQL语句，从OrderItems表中检索出所有`不同`订单号（order_num），其中包含100个或更多的产品。
```SQL
SELECT DISTINCT order_num
FROM OrderItems
WHERE quantity >= 100;
```
4．编写SQL语句，返回Products表中所有价格在3美元到6美元之间的产品的名称（prod_name）和价格（prod_price），然后按价格对结果进行排序。（本题有多种解决方案，我们在下一课再讨论，不过你可以使用目前已学的知识来解决它。）
```SQL
SELECT prod_name, prod_price
FROM Products
WHERE prod_price BETWEEN 3 AND 6
ORDER BY prod_price;
```
## 第5课 高级数据过滤
1．编写SQL语句，从Vendors表中检索供应商名称（vend_name），仅返回加利福尼亚州的供应商（这需要按国家[USA]和州[CA]进行过滤，没准其他国家也存在一个加利福尼亚州）。提示：过滤器需要匹配字符串。
```SQL
SELECT vend_name
FROM Vendors
WHERE vend_country = 'USA' AND vend_state = 'CA';
```
2．编写SQL语句，查找所有至少订购了总量100个的BR01、BR02或BR03的订单。你需要返回OrderItems表的订单号（order_num）、产品ID（prod_id）和数量，并按产品ID和数量进行过滤。提示：根据编写过滤器的方式，可能需要特别注意求值顺序。
```SQL
-- Solution 1
SELECT order_num, prod_id, quantity
FROM OrderItems
WHERE (prod_id = 'BR01' OR prod_id = 'BR02' OR prod_id = 'BR03') AND quantity >= 100;

-- Solution 2
SELECT order_num, prod_id, quantity
FROM OrderItems
WHERE prod_id IN ('BR01', 'BR02', 'BR03') AND quantity >= 100;
```
3．现在，我们回顾上一课的挑战题。编写SQL语句，返回所有价格在3美元到6美元之间的产品的名称（prod_name）和价格（prod_price）。使用AND，然后按价格对结果进行排序。
```SQL
SELECT prod_name, prod_price
FROM Products
WHERE prod_price >= 3 AND prod_price <= 6
ORDER BY prod_price;
```
4．下面的SQL语句有问题吗？（尝试在不运行的情况下指出。）
```SQL
SELECT vend_name
From Vendors
ORDER BY vend_name
WHERE vend_country = 'USA' AND vend_state = 'CA';
```
答案: `ORDER BY`  must came after any `WHERE` clause.