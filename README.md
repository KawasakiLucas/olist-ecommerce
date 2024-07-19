
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
