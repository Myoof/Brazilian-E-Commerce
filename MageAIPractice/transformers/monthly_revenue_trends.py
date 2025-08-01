if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd

@transformer
def transform_monthly_revenue(data, *args, **kwargs):
    df_customers, df_geo, df_order_items, df_payments, df_reviews, df_orders, df_products, df_sellers, df_category_translation = data

    # Merge orders with payments
    df = df_orders.merge(df_payments, on='order_id')

    # Convert timestamp and extract month as YYYY-MM
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
    df['monthofyear'] = df['order_purchase_timestamp'].dt.to_period('M').astype(str)

    # Aggregate revenue by month
    df_grouped = df.groupby('monthofyear').agg(revenue=('payment_value', 'sum')).reset_index()

    # Ensure correct types for export
    df_grouped['monthofyear'] = df_grouped['monthofyear'].astype(str)
    df_grouped['revenue'] = df_grouped['revenue'].astype(float)
       
    return df_grouped
    


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
