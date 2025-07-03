"""
SQL


CREATE SCHEMA dannys_diner;
 CREATE TABLE sales (  "customer_id" VARCHAR(1),  "order_date" DATE,  "product_id" INTEGER );
 INSERT INTO sales  ("customer_id", "order_date", "product_id") VALUES  ('A', '2021-01-01', '1'),  ('A', '2021-01-01', '2'),  ('A', '2021-01-07', '2'),  ('A', '2021-01-10', '3'),  ('A', '2021-01-11', '3'),  ('A', '2021-01-11', '3'),  ('B', '2021-01-01', '2'),  ('B', '2021-01-02', '2'),  ('B', '2021-01-04', '1'),  ('B', '2021-01-11', '1'),  ('B', '2021-01-16', '3'),  ('B', '2021-02-01', '3'),  ('C', '2021-01-01', '3'),  ('C', '2021-01-01', '3'),  ('C', '2021-01-07', '3');
 CREATE TABLE menu (  "product_id" INTEGER,  "product_name" VARCHAR(5),  "price" INTEGER );
 INSERT INTO menu  ("product_id", "product_name", "price") VALUES  ('1', 'sushi', '10'),  ('2', 'curry', '15'),  ('3', 'ramen', '12');
   CREATE TABLE members (  "customer_id" VARCHAR(1),  "join_date" DATE );
 INSERT INTO members  ("customer_id", "join_date") VALUES  ('A', '2021-01-07'),  ('B', '2021-01-09');


























What is the total amount each customer spent at the restaurant?
    SELECT sales.customer_id, SUM(menu.price) AS total_amount
    FROM sales
    JOIN menu ON sales.product_id = menu.product_id
    GROUP BY sales.customer_id;
How many days has each customer visited the restaurant?
    SELECT customer_id, COUNT(DISTINCT order_date) AS visit_days
    FROM sales
    GROUP BY customer_id;
What was the first item from the menu purchased by each customer?
    SELECT sales.customer_id, menu.product_name
    FROM sales
    JOIN menu ON sales.product_id = menu.product_id
    WHERE sales.order_date = (
        SELECT MIN(order_date)
        FROM sales s2
        WHERE s2.customer_id = sales.customer_id
    )
    GROUP BY sales.customer_id, menu.product_name;
What is the most purchased item on the menu and how many times was it purchased by all customers?
    SELECT menu.product_name, COUNT(sales.product_id) AS purchase_count
    FROM sales
    JOIN menu ON sales.product_id = menu.product_id
    GROUP BY menu.product_name
    ORDER BY purchase_count DESC
    LIMIT 1;
Which item was the most popular for each customer?
    SELECT sales.customer_id, menu.product_name, COUNT(sales.product_id) AS purchase_count
    FROM sales
    JOIN menu ON sales.product_id = menu.product_id
    GROUP BY sales.customer_id, menu.product_name
    HAVING purchase_count = (
        SELECT MAX(purchase_count)
        FROM (
            SELECT COUNT(sales.product_id) AS purchase_count
            FROM sales
            WHERE sales.customer_id = s.customer_id
            GROUP BY sales.product_id
        ) AS subquery
    );
Which item was purchased first by the customer after they became a member?
    SELECT sales.customer_id, menu.product_name
    FROM sales
    JOIN members ON sales.customer_id = members.customer_id
    JOIN menu ON sales.product_id = menu.product_id
    WHERE sales.order_date = (
        SELECT MIN(order_date)
        FROM sales s2
        WHERE s2.customer_id = sales.customer_id
        AND s2.order_date >= members.join_date
    )
    GROUP BY sales.customer_id, menu.product_name;
Which item was purchased just before the customer became a member?
    SELECT sales.customer_id, menu.product_name
    FROM sales
    JOIN members ON sales.customer_id = members.customer_id
    JOIN menu ON sales.product_id = menu.product_id
    WHERE sales.order_date = (
        SELECT MAX(order_date)
        FROM sales s2
        WHERE s2.customer_id = sales.customer_id
        AND s2.order_date < members.join_date
    )
    GROUP BY sales.customer_id, menu.product_name;
What is the total items and amount spent for each member before they became a member?
    SELECT members.customer_id, COUNT(sales.product_id) AS total_items, SUM(menu.price) AS total_amount
    FROM sales
    JOIN members ON sales.customer_id = members.customer_id
    JOIN menu ON sales.product_id = menu.product_id
    WHERE sales.order_date < members.join_date
    GROUP BY members.customer_id;
If each $1 spent equates to 10 points and sushi has a 2x points multiplier - how many points would each customer have?
    SELECT members.customer_id,
    SUM(CASE WHEN menu.product_name = 'sushi' THEN menu.price * 20 ELSE menu.price * 10 END) AS total_points
    FROM sales
    JOIN members ON sales.customer_id = members.customer_id
    JOIN menu ON sales.product_id = menu.product_id
    GROUP BY members.customer_id;
In the first week after a customer joins the program (including their join date) they earn 2x points on all items, not just sushi - how many points do customer A and B have at the end of January?
    SELECT members.customer_id,
    SUM(menu.price * 20) AS total_points
    FROM sales
    JOIN members ON sales.customer_id = members.customer_id
    JOIN menu ON sales.product_id = menu.product_id
    WHERE sales.order_date >= members.join_date
    AND sales.order_date < members.join_date + INTERVAL '7 days'
    GROUP BY members.customer_id;
    GROUP BY members.customer_id;
















"""
