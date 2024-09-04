<h1 align="center">Analysis</h1>

> How could Olist increase its profit?

About Olist 🇧🇷:

Olist is a leading e-commerce service that connects merchants to main marketplaces in Brazil. They provide a wide range of offers including inventory management, dealing with reviews and customer contacts to logistic services.

Olist charges sellers a monthly fee. This fee is progressive with the volume of orders.

Here are the seller and customer workflows:

**Seller:**

- Seller joins Olist
- Seller uploads products catalogue
- Seller gets notified when a product is sold
- Seller hands over an item to the logistic carrier

Note: that multiple sellers can be involved in one customer order!

**Customer:**

- Browses products on the marketplace
- Purchases products from Olist.store
- Gets an expected date for delivery
- Receives the order
- Leaves a review about the order

Note: A review can be left as soon as the order is sent, meaning that a customer can leave a review for a product he did not receive yet!

<h2 align="left">Project Structure</h2>

```bash
.
# Your whole code logic and data, this is your "package"
├── data                # data source (git ignored)
|   ├── csv
|   |   ├── olist_customers_dataset.csv
|   |   ├── olist_geolocation_dataset.csv
|   |   ├── olist_order_items_dataset.csv
|   |   ├── olist_order_payments_dataset.csv
|   |   ├── olist_order_reviews_dataset.csv
|   |   ├── olist_orders_dataset.csv
|   |   ├── olist_products_dataset.csv
|   |   ├── olist_sellers_dataset.csv
|   |   └── product_category_name_translation.csv
|   ├── brazil_map
|   |   ├── lim_unidade_federacao_a.cpg       # brazil geodata
|   |   ├── lim_unidade_federacao_a.dbf       # brazil geodata
|   |   ├── lim_unidade_federacao_a.prj       # brazil geodata
|   |   ├── lim_unidade_federacao_a.shp       # brazil geodata
|   |   └── lim_unidade_federacao_a.shx       # brazil geodata
|   └── README.md       # database documentation
|
├── olist               # data-processing logic
|   ├── __init__.py     # turns the olist folder into a "package"
|   ├── data.py
|   ├── order.py
|   ├── product.py
|   ├── review.py
|   ├── seller.py
|   ├── utils.py
|   └── README.md
|
├── notebooks            # analysis
|   ├── exploratory-data-analysis.ipynb
|   ├── statistical-inference-1-orders.ipynb
|   ├── statistical-inference-2-sellers.ipynb
|   ├── statistical-inference-3-products.ipynb
|   ├── conclusion-potential-solutions.ipynb
|   └── README.md

```

Before start, add `olist` path to `PYTHONPATH`.

This will allow you to easily import modules defined in `olist` in your notebooks.


The project is going to be divided in 3 steps:

-  Exploratory Data Analysis (EDA)
-  Statistical Inference
-  Conclusion and Potential Solutions

<h3 align="left">Exploratory Data Analysis (EDA):</h3>

-  Data cleaning and preprocessing
-  Descriptive statistics and summary metrics
-  Identifying key trends, patterns, and anomalies

<h3 align="left">Statistical Inference:</h3>

-  Investigate the orders and their associated review score.
-  Find sellers who have repeatedly been underperforming vs. others and understand why.
-  Find product categories that repeatedly underperform vs. others.

<h3 align="left">Conclusion and Potential Solutions:</h3>

-  How could Olist improve its profit?
-  Should Olist remove underperforming sellers from its marketplace?

<br />
<p align="right"><a href="https://github.com/KawasakiLucas/olist-ecommerce">back to main page -></a></p>
