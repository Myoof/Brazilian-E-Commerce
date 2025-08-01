# from mage_ai.data_preparation.decorators import transformer
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd



@transformer
def transform_clv(data, *args, **kwargs):
    df_customers, df_geo, df_order_items, df_payments, df_reviews, df_orders, df_products, df_sellers, df_category_translation = data
    df = df_orders.merge(df_payments, on='order_id')
    df_grouped = df.groupby('customer_id').agg(
        total_revenue=('payment_value', 'sum'),
        num_orders=('order_id', 'nunique')
    )
    df_grouped['avg_order_value'] = df_grouped['total_revenue'] / df_grouped['num_orders']
    df_grouped.reset_index(inplace=True)
    return df_grouped

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
