
<h1 align="center">OLIST DATASET</h1>

The dataset contains details of 100,000 orders placed between 2016 and 2018 across various marketplaces in Brazil. It includes features that provide a multi-dimensional view of each order, covering aspects such as order status, pricing, payment, freight performance, customer locations, product attributes, and customer reviews. Additionally, a geolocation dataset is available, linking Brazilian zip codes to their corresponding latitude and longitude coordinates.

The data is organized into multiple datasets for improved clarity and structure. Please refer to the following data schema:

<img align="center" src="https://github.com/KawasakiLucas/olist-ecommerce/blob/master/images/olist-data-scheme.png">

Source: **[Kaggle - Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)**

There are 9 csv files (~120mb) placed on data/csv folder as follow:

- <a href="#olist_customers_dataset">**olist_customers_dataset**</a>
- <a href="#olist_geolocation_dataset">**olist_geolocation_dataset**</a>
- <a href="#olist_order_items_dataset">**olist_order_items_dataset**</a>
- <a href="#olist_order_payments_dataset">**olist_order_payments_dataset**</a>
- <a href="#olist_order_reviews_dataset">**olist_order_reviews_dataset**</a>
- <a href="#olist_orders_dataset">**olist_orders_dataset**</a>
- <a href="#olist_products_dataset">**olist_products_dataset**</a>
- <a href="#olist_sellers_dataset">**olist_sellers_dataset**</a>
- <a href="#product_category_name_translation">**product_category_name_translation**</a>


<h2 align="left">olist_customers_dataset</h2>

This dataset has information about the customer and their location. Use it to identify unique customers in the orders dataset and to find the orders delivery location.

- `customer_id`: key to the orders dataset. Each order has a unique customer_id.
- `customer_unique_id`: unique identifier of a customer.
- `customer_zip_code_prefix`: first five digits of customer zip code
- `customer_city`: customer city name
- `customer_state`: customer state


<h2 align="left">olist_geolocation_dataset</h2>

This dataset has information about Brazilian zip codes and lat/lng coordinates. Use it to plot maps and find distances between sellers and customers.

- `geolocation_zip_code_prefix`: first 5 digits of zip code
- `geolocation_lat`: latitude
- `geolocation_lng`: longitude
- `geolocation_city`: city name
- `geolocation_state`: state

<h2 align="left">olist_order_items_dataset</h2>

This dataset includes data about the items purchased within each order.

⚠️ If 3 items are purchased in an order, the dataset will display one row per item. If the same product is bought twice, 2 rows will be displayed.

- `order_id`: order unique identifier
- `order_item_id`: sequential number identifying number of items included in the same order.
- `product_id`: product unique identifier
- `seller_id`: seller unique identifier
- `shipping_limit_date`: shows the seller shipping limit date for handling the order over to the logistic partner.
- `price`: item price
- `freight_value`: item freight value (if an order has more than one item the freight value is split between items)

<h2 align="left">olist_order_payments_dataset</h2>

This dataset includes data about order payment options.

- `order_id`: unique identifier of an order.
- `payment_sequential`: a customer may pay for an order with more than one payment method. If they do, a sequence will be created to accommodate all payments.
- `payment_type`: method of payment chosen by the customer.
- `payment_installments`: number of installments chosen by the customer.
- `payment_value`: transaction value.

<h2 align="left">olist_order_reviews_dataset</h2>

This dataset includes data about the reviews made by a customer.

After a customer purchases the product from the Olist Store, a seller gets notified to fulfill that order. Once the customer receives the product, or the estimated delivery date is due, the customer gets a satisfaction survey by email where they can leave a note for the purchase experience and write some comments.

- `review_id`: unique review identifier
- `order_id`: unique order identifier
- `review_score`: score ranging from 1 to 5 given by the customer on a satisfaction survey.
- `review_comment_title`: title from the review left by the customer, in Portuguese.
- `review_comment_message`: message from the review left by the customer, in Portuguese.
- `review_creation_date`: shows the date in which the satisfaction survey was sent to the customer.
- `review_answer_timestamp`: shows the satisfaction survey response timestamp.

<h2 align="left">olist_orders_dataset</h2>

This is the core dataset. For each order, you can find all other information.

- `order_id`: unique identifier of the order.
- `customer_id`: key to the customer dataset. Each order has a unique customer_id.
- `order_status`: reference to the order status (delivered, shipped, etc).
- `order_purchase_timestamp`: shows the purchase timestamp.
- `order_approved_at`: shows the payment approval timestamp.
- `order_delivered_carrier_date`: shows the order posting timestamp, i.e. when it was handed to the logistic partner.
- `order_delivered_customer_date`: shows the actual order delivery date to the customer.
- `order_estimated_delivery_date`: shows the estimated delivery date that was informed to the customer at the time of purchase.

<h2 align="left">olist_products_dataset</h2>

This dataset includes data about the products sold by Olist.

- `product_id`: unique product identifier
- `product_category_name`: root category of product, in Portuguese.
- `product_name_length`: number of characters extracted from the product name.
- `product_description_length`: number of characters extracted from the product description.
- `product_photos_qty`: number of product published photos
- `product_weight_g`: product weight measured in grams.
- `product_length_cm`: product length measured in centimeters.
- `product_height_cm`: product height measured in centimeters.
- `product_width_cm`: product width measured in centimeters.

<h2 align="left">olist_sellers_dataset</h2>

This dataset includes data about the sellers that fulfilled orders made at Olist. Use it to find the seller location and to identify which seller fulfilled each product.

- `seller_id`: seller unique identifier
- `seller_zip_code_prefix`: first 5 digits of seller zip code
- `seller_city`: seller city name
- `seller_state`: seller state


<h2 align="left">product_category_name_translation</h2>

Translates the product_category_name to English.

- `product_category_name`: category name in Portuguese
- `product_category_name_english`: category name in English

<br />
<p align="right">(<a href="https://github.com/KawasakiLucas/olist-ecommerce/tree/master">back to main page</a>)</p>
