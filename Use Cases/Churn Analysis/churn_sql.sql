/*
Data Tables
events: [ userid | event_timestamp | event_type | product_id ]
a log/transaction dataset with the events on your website, what page users see, what product they like or purchase

product: [ product_id | category | price ]
a lookup table containing the product_id and information about its category and price

Churner - a customer that hasn't taken any action on the website for four months
We also want to restrict our dataset to customers who have made at least one purchase in the four months previous to the reference date for a total amount greater than 30.
That way we are only looking at people we consider to be high-value customers
The target churner variable is built by looking ahead over a four  month period from a reference data and flagging customers if they purchsaed a product in this tie frame.
*/


--------- 1. Join our two datasets to create a new table [events_complete]
SELECT * FROM events e 
LEFT JOIN products p ON e.product_id = p.product_id

----------2. Restrict the training set to customers that spend more than $30. This will create a new table [train_active_clients]
Select * FROM(
  SELECT user_id, sum(price::numeric) as total_bought
  FROM events_complete events
  WHERE event_timestamp < TIMESTAMP '2014-08-01 00:00:00'
  AND event_timestamp >= TIMESTAMP '2014-08-01 00:00:00' - INTERVAL '4 months'
  AND event_type = "buy_order"
  GROUP BY user_id) customers
WHERE total_bought>=30

-----------3. Define our churner target for the training set by creating the table [train]
SELECT customer.user_id, 
  CASE WHEN loyal.user_id IS NULL THEN 1
  ELSE 0
  END as target
FROM tarin_active_clients customer
LEFT JOIN (--- users that actually bought something in the following 4 months
  SELECT distinct user_id
  FROM events_complete
  WHERE event_timestamp >= TIMESTAMP '2014-08-01 00:00:00'
  AND event_timestamp < TIMESTAMP '2014-08-01 00:00:00' + INTERVAL '4 months'
  AND event_type = 'buy_order') loyal 
  ON customer.user_id = loyal.user_id)

/* If we are interested in enriching our dataset, some further features we could include are
- Number of actions in the last 5 days (10 days, 30 days, etc.)
- Average length of those actions
- Average and max "sleep" time in between actions
- Distribution of hourly activity
- Distribution of day and week activity
*/

---------Data enrichment: generate new features, number of product purchased per category, total amount spend time, time since last purchase, for the train set
SELECT train.*,
  nb_products_seen,
  nb_distinct_product,
  nb_dist_0 , nb_dist_1, nb_dist_2,
  amount_bought , nb_product_bought,
  active_time
FROM train
LEFT JOIN ( -- generate features based on past data
 SELECT user_id,
  COUNT(product_id) AS nb_products_seen,
  COUNT(distinct product_id) AS nb_distinct_product,
  COUNT(distinct category_id_0) AS nb_dist_0,
  COUNT(distinct category_id_1) AS nb_dist_1,
  COUNT(distinct category_id_2) AS nb_dist_2,
  SUM(price::numeric * (event_type = 'buy_order')::int ) AS amount_bought,
  SUM((event_type = 'buy_order')::int ) AS nb_product_bought,
  EXTRACT(EPOCH FROM (TIMESTAMP '2014-08-01 00:00:00' - MIN(event_timestamp)))/(3600*24)
 AS active_time
 FROM events_complete
 WHERE event_timestamp < TIMESTAMP '2014-08-01 00:00:00'
 GROUP BY user_id) features 
ON train.user_id = features.user_id
