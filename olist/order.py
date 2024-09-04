import pandas as pd
import numpy as np
from olist.utils import haversine_distance
from olist.data import Olist
import functools

class Order:
    '''
    DataFrames containing all orders as index,
    and various properties of these orders as columns
    '''
    def __init__(self):
        # Assign an attribute ".data" to all new instances of Order
        self.data = Olist().get_data()

    def get_wait_time(self, is_delivered=True):
        """
        Returns a DataFrame with:
        [order_id, wait_time, expected_wait_time, delay_vs_expected, order_status]
        and filters out non-delivered orders unless specified
        """
        # Within this instance method, we have access to the instance of the class Order
        # in the variable self, as well as all its attributes
        # Save the data in a copy dataframe
        orders = self.data['orders'].copy()
        # filter delivered orders
        if is_delivered:
            orders = orders.query("order_status=='delivered'").copy()

        # Convert the date object in datetime and assign in the data
        orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
        orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'])
        orders['order_estimated_delivery_date'] = pd.to_datetime(orders['order_estimated_delivery_date'])

        # Compute wait_time and convert to days as a float
        orders['wait_time'] = orders['order_delivered_customer_date'] - orders['order_purchase_timestamp']
        orders['wait_time'] = orders['wait_time'].dt.total_seconds()/(24 * 60 * 60)

        # Compute expected_wait_time and convert to days as a float
        orders['expected_wait_time'] = orders['order_estimated_delivery_date'] - orders['order_purchase_timestamp']
        orders['expected_wait_time'] = orders['expected_wait_time'].dt.total_seconds()/(24 * 60 * 60)

        # Compute delay_vs_expected and convert to days as a float. If delay >= 0 keep the number. Else replace to 0.
        orders['delay_vs_expected'] = orders['order_delivered_customer_date'] - orders['order_estimated_delivery_date']
        orders['delay_vs_expected'] = orders['delay_vs_expected'].dt.total_seconds()/(24 * 60 * 60)
        orders['delay_vs_expected'] = orders['delay_vs_expected'].apply(lambda x: x if x >= 0 else 0)

        # Keep only the interest columns
        orders = orders[['order_id', 'wait_time', 'expected_wait_time', 'delay_vs_expected', 'order_status']]
        return orders

    def get_review_score(self):
        """
        Returns a DataFrame with:
        order_id, dim_is_five_star, dim_is_one_star, review_score
        """
        # Save the data in a copy dataframe
        reviews = self.data['order_reviews'].copy()
        # | `dim_is_five_star` 	| int 	| 1 if the order received a five-star review, 0 otherwise 	|
        reviews['dim_is_five_star'] = reviews['review_score'].apply(lambda x: 1 if x == 5 else 0)
        # | `dim_is_one_star` 	| int 	| 1 if the order received a one_star, 0 otherwise 	|
        reviews['dim_is_one_star'] = reviews['review_score'].apply(lambda x: 1 if x == 1 else 0)
        # Keep only the interest columns
        reviews = reviews[['order_id', 'dim_is_five_star', 'dim_is_one_star', 'review_score']]
        return reviews

    def get_number_products(self):
        """
        Returns a DataFrame with:
        order_id, number_of_products
        """
        # Save the data in a copy dataframe
        products = self.data['products'].copy()
        order_items = self.data['order_items'].copy()
        # Merged the 2 dataframes by 'product_id' column
        merged_order_item_products = (
            order_items[['order_id', 'product_id']].merge(
                products['product_id'], how='inner', on='product_id'
            )
        )
        # Group by 'order_id' and preserve the index
        merged_order_item_products = (
            merged_order_item_products.groupby(
                merged_order_item_products['order_id'], as_index=False
            ).count()
        )
        # Rename the 'product_id' column which became 'number_of_products'
        merged_order_item_products = (
            merged_order_item_products.rename(
                columns={'product_id':'number_of_products'}
            )
        )
        return merged_order_item_products
    def get_number_sellers(self):
        """
        Returns a DataFrame with:
        order_id, number_of_sellers
        """
        # Save the data in a copy dataframe
        sellers = self.data['sellers'].copy()
        order_items = self.data['order_items'].copy()
        # Merged the 2 dataframes by 'seller_id' column
        merged_order_item_sellers = (
            order_items[['order_id', 'seller_id']].merge(
                sellers['seller_id'], how='inner', on='seller_id'
            )
        )
        # Group by 'order_id' and preserve the index
        merged_order_item_sellers = (
            merged_order_item_sellers.groupby(
                merged_order_item_sellers['order_id'], as_index=False
            ).count()
        )
        return merged_order_item_sellers

    def get_price_and_freight(self):
        """
        Returns a DataFrame with:
        order_id, price, freight_value
        """
        # Save the data in a copy dataframe
        order_items = self.data['order_items'].copy()
        order_items = order_items[['order_id', 'price', 'freight_value']] # just order_id , price, freight_value
        # Group by 'order_id' and preserve the index
        order_items = order_items.groupby('order_id', as_index=False).agg({'price':np.sum,
                                                   'freight_value':np.sum})
        return order_items

    def get_distance_seller_customer(self):
        """
        Returns a DataFrame with:
        order_id, distance_seller_customer
        """
        # Save the data in a copy dataframe
        geolocation = self.data['geolocation'].copy()
        customers = self.data['customers'].copy()
        orders = self.data['orders'].copy()
        sellers = self.data['sellers'].copy()
        order_items = self.data['order_items'].copy()

        ###################################################################################
        ###################################################################################
        # Step Sellers
        ###################################################################################
        ###################################################################################
        # Merged order_items and sellers by 'seller_id' column
        orders_sellers = order_items[['order_id', 'seller_id']].merge(
            sellers[['seller_id','seller_zip_code_prefix']], how='inner', on='seller_id')

        # Merged orders_sellers and geolocation by 'zip_code_prefix' column
        geolocation_sellers = pd.merge(
            orders_sellers,
            geolocation[['geolocation_zip_code_prefix', 'geolocation_lat', 'geolocation_lng']],
            how='inner',
            left_on=['seller_zip_code_prefix'],
            right_on = ['geolocation_zip_code_prefix']
        )
        # remove duplicates lines from geolocation_sellers
        geolocation_sellers = geolocation_sellers.drop_duplicates(subset=['order_id'])

        # Rename some columns
        geolocation_sellers = geolocation_sellers[['order_id','seller_id','geolocation_lat','geolocation_lng']]
        geolocation_sellers = geolocation_sellers.rename(columns={'geolocation_lat':'seller_geolocation_lat',
                                                                  'geolocation_lng':'seller_geolocation_lng'})

        ###################################################################################
        ###################################################################################
        # Step Custormers
        ###################################################################################
        ###################################################################################
        # Merged orders and customers by 'customer_id' column
        orders_customers = orders[['order_id', 'customer_id']].merge(
            customers[['customer_id','customer_zip_code_prefix']], how='inner', on='customer_id')

        # Merged orders_customers and geolocation by 'zip_code_prefix' column
        geolocation_customers = pd.merge(
            orders_customers,
            geolocation[['geolocation_zip_code_prefix', 'geolocation_lat', 'geolocation_lng']],
            how='inner',
            left_on=['customer_zip_code_prefix'],
            right_on = ['geolocation_zip_code_prefix']
        )
        # remove duplicates lines from geolocation_customers
        geolocation_customers = geolocation_customers.drop_duplicates(subset=['order_id'])

        # Rename some columns
        geolocation_customers = geolocation_customers[['order_id','customer_id','geolocation_lat','geolocation_lng']]
        geolocation_customers = geolocation_customers.rename(columns={'geolocation_lat':'customer_geolocation_lat',
                                                                      'geolocation_lng':'customer_geolocation_lng'})

        ###################################################################################
        ###################################################################################
        # Merge all together
        ###################################################################################
        ###################################################################################
        # Merged geolocation_sellers and geolocation_customers by 'geolocation_zip_code_prefix' column
        geolocation_customers_sellers = pd.merge(geolocation_sellers,
            geolocation_customers, how='inner', on='order_id')

        # Calculate distances
        geolocation_customers_sellers['distance_seller_customer'] = (
            geolocation_customers_sellers.apply(
                lambda x: haversine_distance(
                    x['seller_geolocation_lng'],
                    x['seller_geolocation_lat'],
                    x['customer_geolocation_lng'],
                    x['customer_geolocation_lat']
                ), axis=1
            )
        )

        # Preserve only 'order_id' and 'distance_seller_customer' columns
        geolocation_customers_sellers = geolocation_customers_sellers[['order_id','distance_seller_customer']]
        return geolocation_customers_sellers

    def get_training_data(self,is_delivered=True):
        """
        Returns a clean DataFrame (without NaN), with the all following columns:
        ['order_id', 'wait_time', 'expected_wait_time', 'delay_vs_expected',
        'order_status', 'dim_is_five_star', 'dim_is_one_star', 'review_score',
        'number_of_products', 'number_of_sellers', 'price', 'freight_value',
        'distance_seller_customer']
        """
        # re-using our instance methods defined above

        # Group all dataframes in a list
        training_data = [
            Order().get_wait_time(is_delivered),
            Order().get_review_score(),
            Order().get_number_products(),
            Order().get_number_sellers(),
            Order().get_price_and_freight(),
            Order().get_distance_seller_customer()
        ]
        # Merge all dataframes
        training_data = (
            functools.reduce(
                lambda left,right: pd.merge(
                    left, right, on=['order_id'], how='inner'
                ), training_data
            )
        )
        training_data = training_data.rename(columns={'seller_id':'number_of_sellers'})

        training_data = training_data[['delay_vs_expected',
                   'dim_is_five_star',
                   'dim_is_one_star',
                   'expected_wait_time',
                   'freight_value',
                   'number_of_products',
                   'number_of_sellers',
                   'order_id',
                   'order_status',
                   'price',
                   'review_score',
                   'wait_time',
                   'distance_seller_customer']
                   ]
        training_data = training_data.dropna()
        return training_data
