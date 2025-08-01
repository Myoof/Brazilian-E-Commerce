from mage_ai.io.postgres import Postgres

# Make sure this matches the order in your load block
table_names = [
    'olist_customers_dataset',
    'olist_geolocation_dataset',
    'olist_order_items_dataset',
    'olist_order_payments_dataset',
    'olist_order_reviews_dataset',
    'olist_orders_dataset',
    'olist_products_dataset',
    'olist_sellers_dataset',
    'product_category_name_translation',
]

# If your load block returned the list as `output`, use it directly
dataframes = output  # This will be the list of 9 DataFrames

# Export each one to PostgreSQL
for df, table in zip(dataframes, table_names):
    Postgres.with_config('postgres_local').export(
        df,
        'public',
        table,
        if_exists='replace'  # or 'append' if you'd like to keep existing data
    )