<h1 name="readme-top" align="center">OLIST E-Commerce</h1>

<img align="center" src="https://github.com/KawasakiLucas/olist-ecommerce/blob/master/images/OLIST.svg">

Image: **[olist.com](https://olist.com/)**

<h2 align="left">About the project</h2>

This repository contains the code, analysis and some insights conducted on Brazilian E-commerce Public Dataset of orders made at Olist Store.

The primary goal is to find ways to increase customer satisfaction and profit margins while keeping order volumes healthy and minimizing the costs associated with bad reviews.

Please feel free to contact me:
<p align="left">
  <a href="https://www.linkedin.com/in/lucas-kawasaki/">
    <img align="left" width="40" height="40" src="https://github.com/KawasakiLucas/olist-ecommerce/blob/master/images/LI-In-Bug.png">
  </a>
</p>
<p align="left">
  <a href="https://www.wantedly.com/id/lucas_kawasaki">
    <img align="left" width="40" height="40" src="https://github.com/KawasakiLucas/olist-ecommerce/blob/master/images/Wantedly_Mark_DarkBG.png">
  </a>
</p>
<p align="left">
  <a href="https://github.com/KawasakiLucas/portfolio">
    <img align="left" width="40" height="40" src="https://github.com/KawasakiLucas/olist-ecommerce/blob/master/images/github-mark-white.png">
  </a>
</p>

<br />
<h2 align="left">Context</h2>

This dataset was provided by Olist on Kaggle. Olist connects small businesses from across Brazil to various sales channels through a single and simplified contract. These merchants can sell their products via Olist Store and utilize Olist’s logistics partners to ship directly to customers. For more information, visit their website: **[olist.com](https://olist.com/)**

When a customer purchases a product from the Olist Store, the seller is notified to fulfill the order. After the customer receives the product or when the estimated delivery date passes, they receive a satisfaction survey via email. In this survey, customers can rate their purchase experience and leave comments.

<h2 align="left">Dataset</h2>

The dataset contains details of 100,000 orders placed between 2016 and 2018 across various marketplaces in Brazil. It includes features that provide a multi-dimensional view of each order, covering aspects such as order status, pricing, payment, freight performance, customer locations, product attributes, and customer reviews. Additionally, a geolocation dataset is available linking Brazilian zip codes to their corresponding latitude and longitude coordinates.

The data is organized into multiple datasets for improved clarity and structure. Please refer to the following data schema:

<img align="center" src="https://github.com/KawasakiLucas/olist-ecommerce/blob/master/images/olist-data-scheme.png">

Image: **[Kaggle - Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)**

There are 9 csv files (~120mb) placed on data/csv folder as follow:

- Customers Dataset
- Geolocation Dataset
- Order items Dataset
- Order Payments Dataset
- Order Reviews Dataset
- Orders Dataset
- Products Dataset
- Sellers Dataset
- Product Category Name Translation

<p align="left"><a href="https://github.com/KawasakiLucas/olist-ecommerce/tree/master/data">You can check the dataset information here -></a></p>

<h2 align="left">Project Structure</h2>

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
-  Should Olist remove under-performing sellers from its marketplace?

<p align="left"><a href="https://github.com/KawasakiLucas/olist-ecommerce/tree/master/analysis">You can check the analysis here -></a></p>


<h2 align="left">Tools</h2>


<img align="left" width="40" height="40" src="https://github.com/KawasakiLucas/olist-ecommerce/blob/master/images/svg/python.svg">
<img align="left" width="40" height="40" src="https://github.com/KawasakiLucas/olist-ecommerce/blob/master/images/svg/pandas.svg">
<img align="left" width="40" height="40" src="https://github.com/KawasakiLucas/olist-ecommerce/blob/master/images/svg/numpy.svg">
<img align="left" width="40" height="40" src="https://github.com/KawasakiLucas/olist-ecommerce/blob/master/images/svg/git.svg">
<img align="left" width="40" height="40" src="https://github.com/KawasakiLucas/olist-ecommerce/blob/master/images/svg/jupyter.svg">
<img align="left" width="40" height="40" src="https://github.com/KawasakiLucas/olist-ecommerce/blob/master/images/svg/plot_ly.svg">

<h2 align="left"></h2>

<br />
<h2 align="left">Acknowledgements</h2>

Thanks to Olist for releasing this dataset.

<br />
<p align="right"><a href="#readme-top">back to the top -></a></p>
