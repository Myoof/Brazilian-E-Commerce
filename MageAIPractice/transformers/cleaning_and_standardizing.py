if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd

@transformer
def transform_clean_orders(data, *args, **kwargs):
    df_customers, df_geo, df_order_items, df_payments, df_reviews, df_orders, df_products, df_sellers, df_category_translation = data
    df = df_orders.copy()
    df = df.drop_duplicates()
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'], errors='coerce')
    df = df.dropna(subset=['order_id', 'customer_id', 'order_purchase_timestamp'])
    return df

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
