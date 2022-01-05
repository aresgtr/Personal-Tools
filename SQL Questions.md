# SQL必知必会第五版练习笔记
## 数据库例
### Products
| prod_id | prod_name | prod_price | vend_id | prod_desc|
| --- | --- | --- | --- | --- |
| BNBG01 | Fish bean bag toy | 3.49 | BRS01 |   |
| BR01   | 8 inch teddy bear | 5.99 | DLL01 |   |
### Customers
| cust_id | cust_name | cust_email |
| --- | --- | --- |
| 01 | Kids Place | |
| 02 | The Toy Store | |
### Orders
| order_num | cust_id | order_date |
| --- | --- | --- |
### OrderItems
| order_num | prod_id | quantity| item_price |
| --- | --- | --- | --- |
### Vendors
| vend_id | vend_name | vend_country | vend_state | vend_address | vend_city |
| --- | --- | --- | --- | --- | --- |
| BRS01 |  | USA| CA|   |   |
| DLL01 |  | USA| CA|   |   |
## 第2课 检索数据
1．编写SQL语句，从Customers表中检索所有的ID（cust_id）。
```SQL
SELECT cust_id
FROM Customers;
```
2．OrderItems表包含了所有已订购的产品（有些已被订购多次）。编写SQL语句，检索并列出已订购产品（prod_id）的清单（不用列每个订单，只列出不同产品的清单）。提示：最终应该显示7行。
```SQL
SELECT DISTINCT prod_id
FROM OrderItems;
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
## 第6课 用通配符进行过滤
1．编写SQL语句，从Products表中检索产品名称（prod_name）和描述（prod_desc），仅返回描述中包含toy一词的产品。
```SQL
SELECT prod_name, prod_desc
FROM Products
WHERE prod_desc LIKE '%toy%';
```
2．反过来再来一次。编写SQL语句，从Products表中检索产品名称（prod_name）和描述（prod_desc），仅返回描述中未出现toy一词的产品。这次，按产品名称对结果进行排序。
```SQL
SELECT prod_name, prod_desc
FROM Products
WHERE NOT prod_desc LIKE '%toy%'
ORDER BY prod_name;
```
3．编写SQL语句，从Products表中检索产品名称（prod_name）和描述（prod_desc），仅返回描述中同时出现toy和carrots的产品。有好几种方法可以执行此操作，但对于这个挑战题，请使用AND和两个LIKE比较。
```SQL
SELECT prod_name, prod_desc
FROM Products
WHERE prod_desc LIKE '%toy%' AND prod_desc LIKE '%carrots%';
```
4．来个比较棘手的。我没有特别向你展示这个语法，而是想看看你根据目前已学的知识是否可以找到答案。编写SQL语句，从Products表中检索产品名称（prod_name）和描述（prod_desc），仅返回在描述中以先后顺序同时出现toy和carrots的产品。提示：只需要用带有三个%符号的LIKE即可。
```SQL
SELECT prod_name, prod_desc
FROM Products
WHERE prod_desc LIKE '%toy%carrots%';
```
## 第7课 创建计算字段
1．别名的常见用法是在检索出的结果中重命名表的列字段（为了符合特定的报表要求或客户需求）。编写SQL语句，从Vendors表中检索vend_id、vend_name、vend_address和vend_city，将vend_name重命名为vname，将vend_city重命名为vcity，将vend_address重命名为vaddress。按供应商名称对结果进行排序（可以使用原始名称或新的名称）。
```SQL
SELECT vend_id,
    vend_name AS vname,
    vend_address AS vaddress,
    vend_city AS vcity
FROM Vendors
ORDER BY vname;
```
2．我们的示例商店正在进行打折促销，所有产品均降价10%。编写SQL语句，从Products表中返回prod_id、prod_price和sale_price。sale_price是一个包含促销价格的计算字段。提示：可以乘以0.9，得到原价的90%（即10%的折扣）。
```SQL
SELECT prod_id, prod_price,
    sale_price AS prod_price * 0.9
FROM Products;
```
## 第8课 使用函数处理数据
1．我们的商店已经上线了，正在创建顾客账户。所有用户都需要登录名，默认登录名是其名称和所在城市的组合。编写SQL语句，返回顾客ID（cust_id）、顾客名称（customer_name）和登录名（user_login），其中登录名全部为大写字母，并由顾客联系人的前两个字符（cust_contact）和其所在城市的前三个字符（cust_city）组成。例如，我的登录名是BEOAK（Ben Forta，居住在OakPark）。提示：需要使用函数、拼接和别名。
```SQL
-- DB2, PostgreSQL
SELECT cust_id, cust_name,
        UPPER(LEFT(cust_contact, 2)) || UPPER(LEFT(cust_city, 3)) AS user_login
FROM customers;
-- Oracle, SQLite
SELECT cust_id, cust_name,
        UPPER(SUBSTR(cust_contact, 1, 2)) || UPPER(SUBSTR(cust_city, 1, 3)) AS user_login
 FROM customers;
-- MySQL
SELECT cust_id, cust_name,
        CONCAT(UPPER(LEFT(cust_contact, 2)), UPPER(LEFT(cust_city, 3))) AS user_login
FROM customers;
-- SQL Server
SELECT cust_id, cust_name,
        UPPER(LEFT(cust_contact, 2)) + UPPER(LEFT(cust_city, 3)) AS user_login
FROM customers;
```
2．编写SQL语句，返回2020年1月的所有订单的订单号（order_num）和订单日期（order_date），并按订单日期排序。你应该能够根据目前已学的知识来解决此问题，但也可以开卷查阅DBMS文档。
```SQL
-- DB2, MariaDB, MySQL
SELECT order_num, order_date
FROM Orders
WHERE YEAR(order_date) = 2020 AND MONTH(order_date) = 1
ORDER BY order_date;
-- Oracle, PostgreSQL
SELECT order_num, order_date
FROM Orders
WHERE EXTRACT(year FROM order_date) = 2020 AND EXTRACT(month FROM order_date) = 1
ORDER BY order_date;
-- PostgreSQL
SELECT order_num, order_date
FROM Orders
WHERE DATE_PART('year', order_date) = 2020
 AND DATE_PART('month', order_date) = 1
ORDER BY order_num;
-- SQL Server
SELECT order_num, order_date
FROM Orders
WHERE DATEPART(yy, order_date) = 2020 AND DATEPART(mm, order_date) = 1
ORDER BY order_date;
-- SQLite
SELECT order_num
FROM Orders
WHERE strftime('%Y', order_date) = '2020'
 AND strftime('%m', order_date) = '01';
```
## 第9课 汇总数据
1．编写SQL语句，确定已售出产品的总数（使用OrderItems中的quantity列）。
```SQL
SELECT SUM(quantity) AS items_ordered
FROM OrderItems;
```
2．修改刚刚创建的语句，确定已售出产品项（prod_id）BR01的总数。
```SQL
SELECT SUM(quantity) AS items_ordered
FROM OrderItems
WHERE prod_id = 'BR01';
```
3．编写SQL语句，确定Products表中价格不超过10美元的最贵产品的价格（prod_price）。将计算所得的字段命名为max_price
```SQL
SELECT MAX(prod_price) AS max_price
FROM Products
WHERE prod_price <= 10;
```
## 第10课 分组数据
1．OrderItems表包含每个订单的每个产品。编写SQL语句，返回每个订单号（order_num）各有多少行数（order_lines），并按order_lines对结果进行排序。
```SQL
SELECT order_num, COUNT(*) AS order_lines
FROM OrderItems
GROUP BY order_num
ORDER BY order_lines;
```
2．编写SQL语句，返回名为cheapest_item的字段，该字段包含每个供应商成本最低的产品（使用Products表中的prod_price），然后从最低成本到最高成本对结果进行排序
```SQL
SELECT vend_id, MIN(prod_price) AS cheapest_item
FROM Products
GROUP BY vend_id
ORDER BY cheapest_item;
```
3．确定最佳顾客非常重要，请编写SQL语句，返回至少含100项的所有订单的订单号（OrderItems表中的order_num）。
```SQL
SELECT order_num
FROM OrderItems
Group BY order_num
HAVING SUM(quantity) >= 100
ORDER BY order_num;
```
4．确定最佳顾客的另一种方式是看他们花了多少钱。编写SQL语句，返回总价至少为1000的所有订单的订单号（OrderItems表中的order_num）。提示：需要计算总和（item_price乘以quantity）。按订单号对结果进行排序。
```SQL
SELECT order_num, SUM(item_price*quantity) AS total_price
FROM OrderItems
GROUP BY order_num
HAVING SUM(item_price*quantity) >= 1000
ORDER BY order_num;
```
5．下面的SQL语句有问题吗？（尝试在不运行的情况下指出。）
```SQL
SELECT order_num, COUNT(*) AS items
FROM OrderItems
GROUP BY items
HAVING COUNT(*) >= 3
ORDER BY items, order_num;
```
答案: `GROUP BY` items is incorrect. `GROUP BY` must be an actual column, not the one being used to perform the aggregate calculations. `GROUP BY` order_num would be allowed.
## 第11课 使用子查询
1．使用子查询，返回购买价格为10美元或以上产品的顾客列表。你需要使用OrderItems表查找匹配的订单号（order_num），然后使用Order表检索这些匹配订单的顾客ID（cust_id）。
```SQL
SELECT cust_id
FROM Order
WHERE order_num IN (
        SELECT order_num
        FROM OrderItems
        WHERE item_price >= 10
);
```
2．你想知道订购BR01产品的日期。编写SQL语句，使用子查询来确定哪些订单（在OrderItems中）购买了prod_id为BR01的产品，然后从Orders表中返回每个产品对应的顾客ID（cust_id）和订单日期（order_date）。按订购日期对结果进行排序。
```SQL
SELECT cust_id, order_date
FROM Orders
WHERE order_num IN (
        SELECT order_num
        FROM OrderItems
        WHERE prod_id = 'BR01'
)
ORDER BY order_date;
```
3．现在我们让它更具挑战性。在上一个挑战题，返回购买prod_id为BR01的产品的所有顾客的电子邮件（Customers表中的cust_email）。提示：这涉及SELECT语句，最内层的从OrderItems表返回order_num，中间的从Customers表返回cust_id。
```SQL
SELECT cust_email
FROM Customers
WHERE cust_id IN (
        SELECT cust_id
        FROM Orders
        WHERE order_num IN (
                SELECT order_num
                FROM OrderItems
                WHERE prod_id = 'BR01'
        )
);
```
4．我们需要一个顾客ID列表，其中包含他们已订购的总金额。编写SQL语句，返回顾客ID（Orders表中的cust_id），并使用子查询返回total_ordered以便返回每个顾客的订单总数。将结果按金额从大到小排序。提示：你之前已经使用SUM()计算订单总数。
```SQL
SELECT cust_id, (
        SELECT SUM(item_price*quantity)
        FROM OrderItems
        WHERE Orders.order_num = OrderItems.order_num
) AS total_ordered
FROM Orders
ORDER BY total_ordered DESC;
```
5．再来。编写SQL语句，从Products表中检索所有的产品名称（prod_name），以及名为quant_sold的计算列，其中包含所售产品的总数（在OrderItems表上使用子查询和SUM(quantity)检索）。
```SQL
SELECT prod_name, (
        SELECT SUM(quantity)
        FROM OrderItems
        WHERE Products.prod_id = OrderItems.prod_id
) AS quant_sold
FROM Products;
```
## 第12课 联结表
1．编写SQL语句，返回Customers表中的顾客名称（cust_name）和Orders表中的相关订单号（order_num），并按顾客名称再按订单号对结果进行排序。实际上是尝试两次，一次使用简单的等联结语法，一次使用INNER JOIN。
```SQL
-- Equijoin syntax
SELECT cust_name, order_num
FROM Customers, Orders
WHERE Customers.cust_id = Orders.cust_id
ORDER BY cust_name, order_num;

-- ANSI INNER JOIN syntax
SELECT cust_name, order_num
FROM Customers
INNER JOIN Orders ON Customers.cust_id = Orders.cust_id
ORDER BY cust_name, order_num;
```