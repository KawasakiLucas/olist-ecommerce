
<h1 align="center">OLIST E-Commerce</h1>

<img align="center" src="https://github.com/KawasakiLucas/olist-ecommerce/blob/master/images/OLIST.svg">

Source: **[olist.com](https://olist.com/)**

This repository contains the code, analysis and some insights conducted on Brazilian E-commerce Public Dataset of orders made at Olist Store.

The primary goal is to find ways to increase customer satisfaction and profit margins while keeping order volumes healthy and minimizing the costs associated with bad reviews.

Please feel free to contact me:
<p align="left">
  <a href="https://www.linkedin.com/in/lucas-kawasaki/">
    <img src="https://skillicons.dev/icons?i=linkedin" />
  </a>
</p>

<h2 align="left">Context</h2>

This dataset was provided by Olist on Kaggle. Olist connects small businesses from across Brazil to various sales channels through a single and simplified contract. These merchants can sell their products via Olist Store and utilize Olist’s logistics partners to ship directly to customers. For more information, visit their website: **[olist.com](https://olist.com/)**

When a customer purchases a product from the Olist Store, the seller is notified to fulfill the order. After the customer receives the product or when the estimated delivery date passes, they receive a satisfaction survey via email. In this survey, customers can rate their purchase experience and leave comments.

<h2 align="left">Dataset</h2>

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

<h3 align="left">olist_customers_dataset</h3>

This dataset has information about the customer and their location. Use it to identify unique customers in the orders dataset and to find the orders delivery location.

- `customer_id`: key to the orders dataset. Each order has a unique customer_id.
- `customer_unique_id`: unique identifier of a customer.
- `customer_zip_code_prefix`: first five digits of customer zip code
- `customer_city`: customer city name
- `customer_state`: customer state


<h3 align="left">olist_geolocation_dataset</h3>

This dataset has information about Brazilian zip codes and lat/lng coordinates. Use it to plot maps and find distances between sellers and customers.

- `geolocation_zip_code_prefix`: first 5 digits of zip code
- `geolocation_lat`: latitude
- `geolocation_lng`: longitude
- `geolocation_city`: city name
- `geolocation_state`: state

<h3 align="left">olist_order_items_dataset</h3>

This dataset includes data about the items purchased within each order.

⚠️ If 3 items are purchased in an order, the dataset will display one row per item. If the same product is bought twice, 2 rows will be displayed.

- `order_id`: order unique identifier
- `order_item_id`: sequential number identifying number of items included in the same order.
- `product_id`: product unique identifier
- `seller_id`: seller unique identifier
- `shipping_limit_date`: shows the seller shipping limit date for handling the order over to the logistic partner.
- `price`: item price
- `freight_value`: item freight value (if an order has more than one item the freight value is split between items)

<h3 align="left">olist_order_payments_dataset</h3>

This dataset includes data about order payment options.

- `order_id`: unique identifier of an order.
- `payment_sequential`: a customer may pay for an order with more than one payment method. If they do, a sequence will be created to accommodate all payments.
- `payment_type`: method of payment chosen by the customer.
- `payment_installments`: number of installments chosen by the customer.
- `payment_value`: transaction value.

<h3 align="left">olist_order_reviews_dataset</h3>

This dataset includes data about the reviews made by a customer.

After a customer purchases the product from the Olist Store, a seller gets notified to fulfill that order. Once the customer receives the product, or the estimated delivery date is due, the customer gets a satisfaction survey by email where they can leave a note for the purchase experience and write some comments.

- `review_id`: unique review identifier
- `order_id`: unique order identifier
- `review_score`: score ranging from 1 to 5 given by the customer on a satisfaction survey.
- `review_comment_title`: title from the review left by the customer, in Portuguese.
- `review_comment_message`: message from the review left by the customer, in Portuguese.
- `review_creation_date`: shows the date in which the satisfaction survey was sent to the customer.
- `review_answer_timestamp`: shows the satisfaction survey response timestamp.

<h3 align="left">olist_orders_dataset</h3>

This is the core dataset. For each order, you can find all other information.

- `order_id`: unique identifier of the order.
- `customer_id`: key to the customer dataset. Each order has a unique customer_id.
- `order_status`: reference to the order status (delivered, shipped, etc).
- `order_purchase_timestamp`: shows the purchase timestamp.
- `order_approved_at`: shows the payment approval timestamp.
- `order_delivered_carrier_date`: shows the order posting timestamp, i.e. when it was handed to the logistic partner.
- `order_delivered_customer_date`: shows the actual order delivery date to the customer.
- `order_estimated_delivery_date`: shows the estimated delivery date that was informed to the customer at the time of purchase.

<h3 align="left">olist_products_dataset</h3>

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

<h3 align="left">olist_sellers_dataset</h3>

This dataset includes data about the sellers that fulfilled orders made at Olist. Use it to find the seller location and to identify which seller fulfilled each product.

- `seller_id`: seller unique identifier
- `seller_zip_code_prefix`: first 5 digits of seller zip code
- `seller_city`: seller city name
- `seller_state`: seller state


<h3 align="left">product_category_name_translation</h3>

Translates the product_category_name to English.

- `product_category_name`: category name in Portuguese
- `product_category_name_english`: category name in English







<br />
<h2 align="left">Project Structure</h2>

The project is going to be divided in 5 steps:

-  Exploratory Data Analysis (EDA):
• Data cleaning and preprocessing
• Descriptive statistics and summary metrics
• Identifying key trends, patterns, and anomalies

-  Statistical Inference:

Statistical Inference - how to improve business margin, given that bad reviews costs a lot of money ?”
As the name implies, statistical inference is all about inferring values based on a limited sample of observations. We will learn how to leverage probabilities and mathematical theorems (see module 3) to try and understand how to extrapolate data from limited samples of observations, as accurately as we can.

Statistical inference involves making predictions based on a limited set of observations. This module teaches you how to use probabilities and mathematical theorems to extrapolate data from samples accurately.

To analyse this data we are going to use Linear and Logistic Regression methods to see how different features influence each other.


-  Conclusion and Potential Solutions:

Based on the EDA results....




























Classified Dataset
We had previously released a classified dataset, but we removed it at Version 6. We intend to release it again as a new dataset with a new data schema. While we don't finish it, you may use the classified dataset available at the Version 5 or previous.

Inspiration
Here are some inspiration for possible outcomes from this dataset.

NLP:
This dataset offers a supreme environment to parse out the reviews text through its multiple dimensions.

Clustering:
Some customers didn't write a review. But why are they happy or mad?

Sales Prediction:
With purchase date information you'll be able to predict future sales.

Delivery Performance:
You will also be able to work through delivery performance and find ways to optimize delivery times.

Product Quality:
Enjoy yourself discovering the products categories that are more prone to customer insatisfaction.

Feature Engineering:
Create features from this rich dataset or attach some external public information to it.

Acknowledgements
Thanks to Olist for releasing this dataset.















<h2 align="left">Dataset</h2>

The dataset used in this project is provided by OLIST and contains information about customer orders, products, sellers, and reviews. The data is stored in multiple CSV files.

<br />
<h2 align="left">Analysis</h2>

<img align="left" src="https://skillicons.dev/icons?i=python,flask">

Backend framework to handle routes for home, about, portfolio and contact pages, along with email configurations using Flask-Mail.

<img align="left" src="https://skillicons.dev/icons?i=javascript">

For dynamic content updates, language switching, storing user preferences, and handling form interactions.

<img align="left" src="https://skillicons.dev/icons?i=css">

Styling for the layout, design, and responsive features to ensure the website is visually appealing across different devices.

<img align="left" src="https://skillicons.dev/icons?i=html">

Modular templates for different sections of the website, ensuring consistency and easy updates.

<br />

This project demonstrates how to create a dynamic, multilingual, and responsive personal portfolio using modern web technologies.
