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